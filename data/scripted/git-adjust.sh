# git-adjust: like git commit --amend
# but works for any commit, not just the most recent

touch main.py read.py read_test.py write.py write_test.py

git add read.py && git commit -m Read  # Missed a file!
git add write*.py && git commit -m Write
git add main.py && git commit -m Main

git st
# oops!

git log --oneline
git adjust -A HEAD~~
git show HEAD~~
