import unittest
from Synthetic_Dataset_Creator import bamsurgeon_handler as bams
import os

test_path = '/home/mire/PycharmProjects/project_test/testfiles/'


class MyTestCase(unittest.TestCase):

    def test_create_mutations(self):
        mutationtype = 'addsnv'
        variationfile = test_path + 'mychr17snv1.bed'
        referencefile = test_path + '/fasta_hg38/hg38.fa'
        bamfile = test_path + 'hg38/NA12878_mybam.sorted.bam'
        outputfile = '/home/mire/PycharmProjects/project_test/bms_output/addsnvtest.bam'
        nr_procs = '30'

        os.chdir('/home/mire/PycharmProjects/project_test/bms_output/')

        bams.create_mutations(mutationtype, variationfile, referencefile, bamfile, outputfile, nr_procs)
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
