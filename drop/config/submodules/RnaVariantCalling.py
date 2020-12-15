from drop import utils
from .Submodules import Submodule


class RVC(Submodule):
    
    def __init__(self, config, sampleAnnotation, processedDataDir, processedResultsDir):
        super().__init__(config, sampleAnnotation, processedDataDir, processedResultsDir)
        self.CONFIG_KEYS = [
            "groups", "knownVCFs", "KGsnps", "millsIndels", "dbSNP", "repeat_mask", "hcArgs", "minAlt"
        ]
        self.name = "RnaVariantCalling"
        self.rnaIDs = self.sa.subsetGroups(self.groups, assay="RVC")
        self.checkSubset(self.rnaIDs, warn=10, error=1)
        self.batchIDs = self.setBatchDict()

    def setDefaultKeys(self, dict_):
        super().setDefaultKeys(dict_)
        setKey = utils.setKey
        dict_ = utils.checkKeys(dict_, keys=["repeat_mask"], check_files=True)
        setKey(dict_, None, "groups", self.sa.getGroups(assay="RVC"))
        setKey(dict_, None, "knownVCFs", [])
        setKey(dict_, None, "repeat_mask", "")
        setKey(dict_, None, "hcArgs", "")
        setKey(dict_, None, "minAlt", 3)
        return dict_

    def setBatchDict(self):
        """
        Retrieve mapping of RNA ID to batch (from RNA_VARIANT_GROUP column)
        :return: dictionary {rnaID: batch}
        """
        if not self.rnaIDs:
            raise ValueError("No RNA IDs found in the group, can not create dictionary")
        batch_dict = dict()
        for key, values in self.rnaIDs.items():
            for v in values:
                if v in batch_dict.keys():
                    raise ValueError("RNA IDs must be unique to the RNA Variant Calling group, can not have an RNA_ID "
                                     "point to multiple RNA_VARIANT_GROUPs")
                utils.setKey(batch_dict, None, v, key)
        return batch_dict

    def getBatch(self, rnaID):
        return self.batchIDs.get(rnaID)

    def getRepeatMask(self, sortedName=False):
        if sortedName:
            ext = self.get("repeat_mask").strip().split('.')[-1]
            return ".".join(self.get("repeat_mask").strip().split('.')[:-1]) + "_sorted." + ext
        else:
            return self.get("repeat_mask")

    def getMinAlt(self):
        return str(self.get("minAlt"))

