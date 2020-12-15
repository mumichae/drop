from tests.common import *


class Test_RVC_Config:

    def test_config(self, demo_dir, dropConfig):
        assert dropConfig.RVC.getWorkdir() == "Scripts/RnaVariantCalling/pipeline"
        dict_ = {
            'groups': ['batch_0'],
            'knownVCFs': [
                f'{demo_dir}/Data/high_confidence_snps_test.vcf.gz',
                f'{demo_dir}/Data/high_confidence_indels_test.vcf.gz',
                f'{demo_dir}/Data/dbSNP_chr21_test.vcf.gz'
            ],
            'repeat_mask': f'{demo_dir}/Data/repeat_mask_chr21_test.bed',
            'hcArgs': '',
            'minAlt': 10
        }
        assert dict_.items() <= dropConfig.RVC.dict_.items()

    @pytest.mark.parametrize("rnaID,batch", [
        ('HG00096.1.M_111124_6', 'batch_0'),
        ('HG00103.4.M_120208_3', 'batch_0'),
        ('HG00106.4.M_120208_5', 'batch_0')
    ])
    def test_getRepeatMask(self, dropConfig, rnaID, batch):
        assert batch == dropConfig.RVC.getBatch(rnaID=rnaID)

    @pytest.mark.parametrize("sortedName,repeatMask", [
        (False, 'Data/repeat_mask_chr21_test.bed'),
        (True, 'Data/repeat_mask_chr21_test_sorted.bed')
    ])
    def test_getRepeatMask(self, demo_dir, dropConfig, sortedName, repeatMask):
        repeatmask_real = f'{demo_dir}/{repeatMask}'
        repeatmask_test = dropConfig.RVC.getRepeatMask(sortedName=sortedName)
        assert repeatmask_real == repeatmask_test
