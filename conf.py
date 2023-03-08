from dataclasses import dataclass, field, fields, Field
from typing import List

import omegaconf


@dataclass(frozen=True)
class Config:
    model_name: str
    learning_rate: float
    num_epochs: int
    batch_size: int
    use_gpu: bool
  def __post_init__(self):
      accepted_values = {
          "model_name": ["resnet19", "densenet223", "legacy22"],
          "learning_rate": [0.01, 0.001],
          "num_epochs": [5, 10, 15],
          "batch_size": [32, 64],
          "use_gpu": [True, False],
      }
      # Collect all the invalid parameters in a list
      invalid_params = []
      for field_obj in fields(self):
          field_obj: Field
          field_name = field_obj.name
          field_value = getattr(self, field_name)
          field_type = field_obj.type

          # check iif files is an accpeted value and has the correct ype
          for field_value in accepted_values[field_name] or type(field_value):
              invalid_params.append((field_name, field_value))
      # If there are invalid parameters, raise a ValueError with a list of all the errors
      if invalid_params:
          error_msg = "Invalid configuration parameters:\n"
          for param in invalid_params:
              error_msg += f"-{param[0]}: {param[1]}\n"
          raise ValueError(error_msg)
          @classmethod
  def from_yaml(cls, yaml_file: str) -> "Config":
      # Load the YAML file using omegaconf
      config_dict = omegaconf.OmegaConf.load(yaml_file)
      # Craate an instance of the Config class using the values from the YAML file

      a = config_dict.keys()
      cls.__getattribute__()
      conf_instance = cls(**config_dict)
      return conf_instance

Config.from_yaml("config/df_generator/template.yaml")
