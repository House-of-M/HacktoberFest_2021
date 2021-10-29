package main

import (
	"bufio"
	"database/sql"
	"fmt"
	_ "github.com/denisenkom/go-mssqldb"
	"github.com/joho/godotenv"
	"log"
	"mssql-go-cli/database"
	"os"
)

func main() {
	envErr := godotenv.Load(); if envErr != nil {
		 fmt.Printf("Error loading credentials: %v", envErr)
	}

	var (
		password = os.Getenv("MSSQL_DB_PASSWORD")
		user = os.Getenv("MSSQL_DB_USER")
	)

	connectionString := fmt.Sprintf("user id=%s;password=%s", user, password)

	sqlInstance, connectionError := sql.Open("mssql", connectionString); if connectionError != nil {
		fmt.Println(fmt.Errorf("error opening database: %v", connectionError))
	}

	data := database.Database{
		SqlDb: sqlInstance,
	}

	fmt.Println("-> Welcome to Reminders Console App, built using Golang and Microsoft SQL Server")
	fmt.Println("-> Select a numeric option; \n [1] Create a new Reminder \n [2] Get a reminder \n [3] Delete a reminder")


	consoleReader := bufio.NewScanner(os.Stdin)
	consoleReader.Scan()
	userChoice := consoleReader.Text()

	switch userChoice {
	case "1":
		var (
			titleInput,
			descriptionInput,
			aliasInput string
		)
		fmt.Println("You are about to create a new reminder. Please provide the following details:")

		fmt.Println("-> What is the title of your reminder?")
		consoleReader.Scan()
		titleInput = consoleReader.Text()

		fmt.Println("-> What is the description of your reminder?")
		consoleReader.Scan()
		descriptionInput = consoleReader.Text()

		fmt.Println("-> What is an alias of your reminder? [ An alias will be needed when deleting your reminder ]")
		consoleReader.Scan()
		aliasInput = consoleReader.Text()

		recordId, err := data.CreateReminder(titleInput, descriptionInput, aliasInput); if err != nil {
		 log.Fatalf("Error from creating reminder: %v", err)
		}

		fmt.Printf("Reminder %v inserted!", recordId)

	case "2":
		getErr := data.RetrieveReminder(); if getErr != nil {
		log.Fatalf("Error retrieving database: %v", getErr)
	    }

	case "3":
		fmt.Println("-> Please provide the alias for the reminder you want to delete:")

		consoleReader.Scan()
		deleteAlias := consoleReader.Text()

		getErr := data.DeleteReminder(deleteAlias); if getErr != nil {
		fmt.Println(getErr)
	}

	default:
		fmt.Printf("-> Option: %v is not a valid numeric option. Try 1 , 2 , 3", userChoice)
	}
}
