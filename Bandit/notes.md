## Bandit Progress Notes

---

### bandit0-1

use ls command to list files  
use cat filename (cat)command to read a file  

password:ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If  

---

### bandit 1-2

used cat ./ filename  

because here filename is '-' if we normally use cat - it recognize dash(-) as a input so to read such files we use  cat ./ filename this format.  

password:263JGJPfgU6LtdEvgfWU1XP5yac29mFx  

---

### bandit 2-3

used cat./"file name"  

as it is string  

password:MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx  

---

### bandit 3-4

used ls  

show the file name inhere in a blur font (not bold)  

so i get inside the directroy using cd command  

i normally used ls to display what files inside this directory but nothing appeared so used ls -a command which gives me a file name . .. ...Hiding-From-You  

i ignored the first 3 dots and considered after as the file name use the cat command  

password:2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ  

---

### bandit 4-5

i normally tried cd inhere went to cd directory and used ls -a command to list all files  

i got set of files but when i used cat command filename in cat "filename"  

i got error  

then i learn about this level  

they used file command to retrive about the file type of each file  

file directory name/*  

it shows the file type of each file then i saw file type assci where all other have data type so that file is differnt so i tried to open using cat "filename"  

it didnt work  

then tried ./ format it opened  

so if the file name contains - in the beginnig use ./ if it is not normal cat if string use ""  
