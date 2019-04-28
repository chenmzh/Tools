# Convert Genbank file to pure sequence file
File = open("C:/Users/User/Dropbox (MIT)/MC0005pKK202.gbk", "r")
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
print("Pure Seq is", Seq)
f = open("C:/Users/User/Dropbox (MIT)/pureseq.txt", "w+")
f.write(Seq)
f.close
