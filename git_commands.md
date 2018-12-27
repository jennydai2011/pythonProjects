
# remove file from history
git filter-branch --force --index-filter 'git rm --cached --ignore-unmatch X.pickle' 
--prune-empty --tag-name-filter cat -- --all

echo "machine\ learning/sentdex/X.pickle" >> .gitignore

#add file to ignore
git commit -m "Add X.pickle to .gitignore"

git rm --cached --ignore-unmatch 'machine learning/.DS_Store'

git filter-branch --force --index-filter \
'git rm --cached --ignore-unmatch machine learning/.DS_Store' \
--prune-empty --tag-name-filter cat -- --all

#remove file from history

git filter-branch --force --index-filter 'git rm -r --cached --ignore-unmatch machine\ learning/sentdex/X.pickle' HEAD
