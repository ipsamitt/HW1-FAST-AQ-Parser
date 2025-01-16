from seqparser import (
        FastaParser,
        FastqParser,
        transcribe,
        reverse_transcribe)

def main():
    """
    The main function
    """
    fastq_file = "data/test.fq"
    parser_obj_fastq = FastqParser(fastq_file)
    for record in parser_obj_fastq:
        print(transcribe(record))

    fasta_file = "data/test.fa"
    parser_obj_fasta = FastaParser(fasta_file)
    for record in parser_obj_fasta:
        print(transcribe(record))   

    for record in parser_obj_fastq:
        print(reverse_transcribe(record))
    for record in parser_obj_fasta:
        print(reverse_transcribe(record))

     
    # Create instance of FastaParser
    # Create instance of FastqParser
        
    # For each record of FastaParser, Transcribe the sequence
    # and print it to console
       
    # For each record of FastqParser, Transcribe the sequence
    # and print it to console


    # For each record of FastaParser, Reverse Transcribe the sequence
    # and print it to console
       
    # For each record of FastqParser, Reverse Transcribe the sequence
    # and print it to console


"""
When executing a python script from the command line there will
always be a hidden variable `__name__` set to the value `__main__`.

Since this is guaranteed you can execute your `main` function with
the following if statement
"""
if __name__ == "__main__":
    main()
