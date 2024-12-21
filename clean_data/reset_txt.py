def reset_txts(out1='storage/output.txt', out2='storage/output2.txt', out3 = 'storage/output.json', out4 = 'storage/output.csv'):
    with open(out1, 'w') as output:
        output.write('')
    with open(out2, 'w') as output:
        output.write('')
    with open(out3, 'w') as output:
        output.write('')
    with open(out4, 'w') as output:
        output.write('')
    print("Done! Cleared output file")