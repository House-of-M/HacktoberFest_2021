 # Note Taker Console Based Application

This folder contains the files for a Console based application written in [Golang](https://golang.org/). Through the application, you can READ, WRITE and DELETE a note within a [Microsoft SQL Server](https://www.microsoft.com/en-us/sql-server/sql-server-2019).

## Prerequisites
To run this application you need the following on your computer;

1. An installation of the [Golang](https://golang.org/) compiler.
2. [Microsoft SQL Server](https://www.microsoft.com/en-us/sql-server/sql-server-2019) installed with a database. A quick way to get a Microsoft SQL Server running is through the [Docker Image installation](https://docs.microsoft.com/en-us/sql/linux/quickstart-install-connect-docker?view=sql-server-ver15).  

## Intsallation
To use the console application, you need to execute the commands outline below;

1. Execiute the command below to install all packages listed in the `go.mod` file;

```bash
go mod tidy
```

2. Create a `.env` file with the following credentials for connecting to a database within the Microsoft SQL Server instance.
```yaml
MSSQL_DB_PASSWORD=<YOUR_MSSQL_SERVER_INSTANCE_PASSWORD>
MSSQL_DB_USER=<YOUR_MSSQL_SERVER_ADMIN_USER>
```

### Learn More; 

The Console application was built using the `go-mssqldb` driver. The Golang guide for Microsoft SQL Server contains several code snippets explaining how the `go-mssqldb` driver operates.