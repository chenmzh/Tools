import matplotlib.pyplot as plt
# open the pure sequence file and read the sequence
localdir = input("Please enter the dir of file here: ")
File = open(localdir, "r")
GenbankFile = File.read()
print("GenbankFile is", GenbankFile)
# Using ORIGIN as the identifier
SeqFile = GenbankFile.split("ORIGIN")[-1]
print("SeqFile is", SeqFile)
Seq = []
for letter in SeqFile:
    if letter in ["a", "t", "c", "g"]:
        Seq += letter
Seq = ''.join(Seq)

# Seq = "attttagcgcgt"

# choose the successive number(how many successive a and t together)
# AT hotpoint criteria: how many a and t appear contuniously. Record the start point from which a and t appear successively
sn = int(input("Please enter the successive number: "))
print(Seq)
# count: record the starting point
count = []
for i in range(len(Seq)-sn+1):
    # record the length of successive a and t
    seq = []
    for j in range(sn):
        if Seq[i+j] in ["a", "t"]:
            seq += Seq[i+j]
        else:
            break
    if len(seq) == sn:
        print(''.join(seq))
        print(i)
        count.append(i+1)
    else:
        continue
print(count)
plt.scatter(count, count, alpha=0.6)
plt.show()
