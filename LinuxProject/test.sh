cat text.txt
echo "Let's learn Linux." >> text.txt
wc -l text.txt
grep "Love" text.txt
sed -i 's/Make/Do/g' text.txt
awk '{print $3}' text.txt
awk '{print NF}' text.txt
