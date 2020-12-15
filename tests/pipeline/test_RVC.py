from tests.common import *


class Test_RVC_Pipeline:

    @pytest.fixture(scope="class")
    def pipeline_run(self, demo_dir):
        LOGGER.info("run RVC pipeline")
        pipeline_run = run(["snakemake", "rnaVariantCalling", f"-j{CORES}"], demo_dir)
        assert "Finished job 0." in pipeline_run.stderr
        return pipeline_run

    @pytest.mark.usefixtures("pipeline_run")
    def test_run(self):
        pass
