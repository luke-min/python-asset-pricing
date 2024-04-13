# python-asset-pricing
Replication of key strategies




## 1. Access to the Data

** [Work in Progress]**

Running this code requires access to WRDS. For obvious security reasons, we cannot publicly share our username or password to WRDS, or share the entire database. The rest of this section assumes you have a valid credential to access WRDS.

You will need to have both `.env` and `.gitignore` files. First, for the `.env` file, you need:

```
WRDS_USER=my_username
WRDSPASSWORD=my_password
```

where you replace the `my_username` and `my_password` with your own username and password for WRDS.

Second, you should also make sure git does not pick up your credentials by adding the following to you `.gitignore`:

```
# ignore all .env files
*.env
```

You may also be asked to authenticate via 2FA.

## 2. Creating the database

Once the above is done, running the code will automatically create a SQL database in your local repository. All the analyses will be done on by pulling data from this database via SQL queries, which are imported to memory as a Pandas dataframe.

## 3. Running Individual Strategies




