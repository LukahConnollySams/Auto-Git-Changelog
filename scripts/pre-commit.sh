#!/bin/sh
# Bash script to obtain git commit message for use in python scripts

CHANGELOG="CHANGELOG.md"
COMMIT_SYNTAX="%B"

# Get commit message and execute python scripts
COMMIT_MESSAGE=$(git log -1 --pretty=%B)

python auto_git_changelog/main.py "$COMMIT_MESSAGE"

# Add changes to changelog to the git commit and continue
git add $CHANGELOG

# Allow user to reject changes/abort commit
while true; do

    echo "Commit changes? (y/n):"
    read RESPONSE

    case "$RESPONSE" in
        [Yy]* ) 
            git commit --amend --no-edit --no-verify # will have to change this later so that other hooks can run after as this will disable all hooks
            exit 0
            ;;

        [Nn]* )
            exit 1
            ;;

        * )
        
            continue
            ;;

    esac

done
