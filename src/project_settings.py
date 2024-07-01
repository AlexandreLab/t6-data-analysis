from pathlib import Path

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
  PATH_BENCHMARK_DATA: Path = Path(r'../data/nd-need-2023-data-tables.xlsx')
  ELECTRICITY_BENCHMARK_SHEET: str = 'Table 9A-9B'
  GAS_BENCHMARK_SHEET: str = 'Table 9C-9D'
  PATH_SAVE_DATA: Path = Path(r'../data/final')
  BENCHMARK_FILENAME: str = 'benchmark_data.csv'
  PATH_ELEC_DATA: Path = Path(r'../data/elec_data.json')
  ELEXON_PROFILES: Path = Path(
      r'../data/Average_Profiling_data_201314_evaluated@10yearNET_v1.0.xlsx')


settings = Settings()

if __name__ == '__main__':
  print(settings.dict())
