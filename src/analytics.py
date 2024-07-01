from dataclasses import dataclass, field

import pandas as pd

from schemas import Sector


@dataclass
class Facility:
  name: str
  floor_area: str
  sector: Sector
  electricity_consumption: pd.DataFrame = field(default_factory=pd.DataFrame)
  gas_consumption: pd.DataFrame = field(default_factory=pd.DataFrame)

  def calculate_electricity_intensity(self) -> float:
    return self.electricity_consumption.sum() / self.floor_area

  def calculate_gas_intensity(self) -> float:
    return self.gas_consumption.sum() / self.floor_area


@dataclass
class Benchmark:
  benchmark_data: pd.DataFrame

  def get_electricity_benchmark(self, sector: Sector) -> float:
    return self.benchmark_data.loc[sector.value,
                                   'Electricity benchmark (kWh/m2)'].value[0]

  def get_gas_benchmark(self, sector: Sector) -> float:
    return self.benchmark_data.loc[sector.value,
                                   'Gas benchmark (kWh/m2)'].value[0]
