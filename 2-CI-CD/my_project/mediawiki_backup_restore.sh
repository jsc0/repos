#!/bin/bash

# MediaWiki Docker container names
MEDIAWIKI_CONTAINER="mediawiki"
DATABASE_CONTAINER="mariadb"

# Paths for backup and restore
BACKUP_DIR="/path/to/backup/directory"
MEDIAWIKI_DIR="/var/www/html"
DB_BACKUP_FILE="mediawiki_backup.sql"
ENCRYPTED_BACKUP_FILE="mediawiki_backup.sql.enc"
GIT_REPO_DIR="/path/to/your/git/repository"

# AWS KMS key ID for encryption
KMS_KEY_ID="your-kms-key-id"

# Function to backup the database
function backup_database {
    echo "Backing up the MediaWiki database..."
    docker exec $DATABASE_CONTAINER mysqldump -u root --password=root_password mediawiki > $BACKUP_DIR/$DB_BACKUP_FILE
    echo "Database backup completed."
}

# Function to backup the MediaWiki files
function backup_files {
    echo "Backing up the MediaWiki files..."
    cp -R $MEDIAWIKI_DIR $BACKUP_DIR
    echo "MediaWiki files backup completed."
}

# Function to encrypt the backup file
function encrypt_backup {
    echo "Encrypting the backup file..."
    aws kms encrypt --key-id $KMS_KEY_ID --plaintext fileb://$BACKUP_DIR/$DB_BACKUP_FILE --output text --query CiphertextBlob > $BACKUP_DIR/$ENCRYPTED_BACKUP_FILE
    echo "Backup file encrypted."
}

# Function to commit and push backup to GitHub
function push_to_github {
    echo "Pushing backup to GitHub..."
    cd $GIT_REPO_DIR || { echo "Failed to change directory."; exit 1; }
    git add .
    git commit -m "MediaWiki backup $(date +'%Y-%m-%d %H:%M:%S')"
    git push origin master
    echo "Backup pushed to GitHub."
}

# Function to restore the database
function restore_database {
    echo "Restoring the MediaWiki database..."
    docker exec -i $DATABASE_CONTAINER mysql -u root --password=root_password mediawiki < $BACKUP_DIR/$DB_BACKUP_FILE
    echo "Database restore completed."
}

# Function to restore the MediaWiki files
function restore_files {
    echo "Restoring the MediaWiki files..."
    cp -R $BACKUP_DIR/html/* $MEDIAWIKI_DIR
    echo "MediaWiki files restore completed."
}

# Main script

echo "MediaWiki Backup and Restore Script"
echo ""
echo "Select an option:"
echo ""
echo "1. Backup MediaWiki"
echo "2. Restore MediaWiki"
echo -n "Enter your choice (1 or 2): "
read choice
echo ""

case $choice in
    1)
        backup_database
        backup_files
        encrypt_backup
        push_to_github
        ;;
    2)
        restore_database
        restore_files
        ;;
    *)
        echo ""
        echo "Invalid choice. Exiting."
        exit 1
        ;;
esac

echo ""
echo "Process completed."

