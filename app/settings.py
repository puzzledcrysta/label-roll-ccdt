import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SAMPLE_ROOT = ROOT / 'sample_data'
DB = Path(os.getenv('WORKBENCH_DB', str(ROOT/'state/ledger.sqlite3')))
TITLE = '卷标追溯核验'
SLUG = 'label-roll'
KEY = '标签卷'
FIELDS = ('计划首号', '计划尾号', '实印号段', '判废号段', '补打号段')
ROLE = '包装产线放行员'
UNIT = '枚'
SIGNATURE = '序号点阵'
RULE_VERSION = 'label-roll-1.0'
TABS = {'intake': '来源采信', 'contract': '字段解释', 'quality': '隔离裁决', 'domain': '补打核销', 'reconcile': '独立对账', 'runs': '批次复算', 'review': '交付复核'}
