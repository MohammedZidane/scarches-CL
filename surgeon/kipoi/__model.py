import os
from collections import OrderedDict

import yaml

from surgeon.models import CVAE


def create_network_yaml(network: CVAE,
                        model_url: str = None,
                        model_md5: str = None,
                        path_to_save: str = "./surgeon.yaml"):
    data = OrderedDict(
        defined_as='kipoi.model.KerasModel',
        args=OrderedDict(
            weights=OrderedDict(
                url=model_url,
                md5=model_md5,
            ),
        ),

        default_dataloader=None,

        info=OrderedDict(
            authors=[
                OrderedDict(
                    name="Mohsen Naghipourfar",
                    github="Naghipourfar",
                    email="mohsen.naghipourfar@gmail.com",
                ),
                OrderedDict(
                    name="Mohammad Lotfollahi",
                    github="M0hammadL",
                    email="mohammad.lotfollahi@helmholtz-muenchen.de",
                ),
            ],
            doc="CVAE model",
            cite_as=None,
            trained_on="Dataset X. held-out Studies A, B, C",
            licence="MIT",
        ),

        dependencies=OrderedDict(  # TODO: Add more depenedencies
            conda=[
                "python=3.6",
                "bioconda::scanpy"
            ],
            pip=[
                "keras>=2.2.0",
            ],
        ),

        schema=OrderedDict(
            inputs=[
                OrderedDict(
                    name="genes",
                    shape=(network.x_dim,),
                ),
                OrderedDict(
                    name="study",
                    shape=(network.n_conditions,),
                    doc="one hot encoded vector of batches (studies)",
                ),
                OrderedDict(
                    name="size_factors",
                    shape=(1,),
                )
            ],
            targets=[
                OrderedDict(
                    name="predicted_genes",
                    shape=(network.x_dim,),
                ),
            ]
        )
    )

    with open(path_to_save, 'w') as outfile:
        yaml.dump(data, outfile, default_flow_style=False)

    print(f"Model YAML has been saved to {os.path.abspath(path_to_save)}!")