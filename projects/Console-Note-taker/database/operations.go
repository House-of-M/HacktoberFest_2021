package database

import (
	"database/sql"
	"fmt"
)

func (db Database) RetrieveReminder() error {
	err := db.SqlDb.PingContext(dbContext); if err != nil {
		return err
	}

	sqlStatement := fmt.Sprintf("SELECT title, description, alias FROM REMINDERS;")

	data, queryErr := db.SqlDb.QueryContext(dbContext, sqlStatement); if queryErr != nil {
		return queryErr
	}

	defer data.Close()

	for data.Next() {
		var title, description, alias string

		nErr := data.Scan(&title, &description, &alias); if nErr != nil {
			return nErr
		}

		fmt.Printf("--> Your Reminder: \n Title: %v \n Description: %v \n Alias: %v \n \n",
		title, description, alias,
			)

		return nil
	}

	return nil
}

func (db Database) CreateReminder(titleInput, aliasInput, descriptionInput string) (int64,  error) {
	var err error

	err = db.SqlDb.PingContext(dbContext); if err != nil {
		return -1, err
	}

	queryStatement :=  `
	INSERT INTO reminders(title, description, alias ) VALUES ('', @Description, @Alias);
	select isNull(SCOPE_IDENTITY(), -1);
	`

	query, err := db.SqlDb.Prepare(queryStatement); if err != nil {
		return -1, err
	}

	defer query.Close()

	newRecord := query.QueryRowContext(dbContext,
		sql.Named("Title", titleInput),
		sql.Named("Description", descriptionInput),
		sql.Named("Alias", aliasInput),
	)

	var newID int64
	err = newRecord.Scan(&newID); if err != nil {
		return -1, err
	}

	return newID, nil
}

func (db Database) DeleteReminder(alias string) error {
	var err error

	err = db.SqlDb.PingContext(dbContext); if err != nil {
		fmt.Printf("Error checking db connection: %v", err)
	}

	queryStatement := `DELETE FROM reminders WHERE alias = @alias;`

	_, err = db.SqlDb.ExecContext(dbContext, queryStatement, sql.Named("alias", alias))
	if err != nil {
		return err
	}

	fmt.Printf("Reminder with %v alias deleted", alias)

	return nil
}