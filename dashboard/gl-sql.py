# https://github.com/weaveworks/grafanalib/blob/v0.7.1/grafanalib/tests/examples/example.dashboard-with-sql.py

import json

from grafanalib._gen import DashboardEncoder
from grafanalib.core import (
    Dashboard,
    Graph,
    GridPos,
    OPS_FORMAT,
    RowPanel,
    SHORT_FORMAT,
    SqlTarget,
    YAxes,
    YAxis,
)


dashboard = Dashboard(
    title="grafana-snippets » grafanalib » Graph and SqlTarget",
    description="Includes a Graph panel using a datasource talking SQL",
    panels=[
        RowPanel(title="New row", gridPos=GridPos(h=1, w=24, x=0, y=8)),
        Graph(
            title="Some SQL Queries",
            dataSource="Your SQL Source",
            targets=[
                SqlTarget(
                    rawSql='SELECT date as "time", metric FROM example WHERE $__timeFilter("time")',
                    refId="A",
                ),
            ],
            yAxes=YAxes(
                YAxis(format=OPS_FORMAT),
                YAxis(format=SHORT_FORMAT),
            ),
            gridPos=GridPos(h=8, w=24, x=0, y=9),
        ),
    ],
).auto_panel_ids()


def encode_dashboard(dashboard) -> str:
    return json.dumps(dashboard, sort_keys=True, cls=DashboardEncoder)


if __name__ == "__main__":
    print(encode_dashboard(dashboard))
