# https://github.com/weaveworks/grafanalib/blob/v0.7.1/grafanalib/tests/examples/example.dashboard.py

import json

from grafanalib._gen import DashboardEncoder
from grafanalib.core import OPS_FORMAT, Dashboard, GaugePanel, GridPos, Target, TimeSeries


dashboard = Dashboard(
    title="grafana-snippets » grafanalib » Random Walk and Default Prometheus",
    description="Includes different panels, using the Random Walk and default Prometheus datasources",
    tags=["example"],
    timezone="browser",
    panels=[
        TimeSeries(
            title="Random Walk",
            dataSource="default",
            targets=[
                Target(
                    datasource="grafana",
                    expr="example",
                ),
            ],
            gridPos=GridPos(h=8, w=16, x=0, y=0),
        ),
        GaugePanel(
            title="Random Walk",
            dataSource="default",
            targets=[
                Target(
                    datasource="grafana",
                    expr="example",
                ),
            ],
            gridPos=GridPos(h=4, w=4, x=17, y=0),
        ),
        TimeSeries(
            title="Prometheus http requests",
            dataSource="prometheus",
            targets=[
                Target(
                    expr="rate(prometheus_http_requests_total[5m])",
                    legendFormat="{{ handler }}",
                    refId="A",
                ),
            ],
            unit=OPS_FORMAT,
            gridPos=GridPos(h=8, w=16, x=0, y=10),
        ),
    ],
).auto_panel_ids()


def encode_dashboard(dashboard) -> str:
    return json.dumps(dashboard, sort_keys=True, cls=DashboardEncoder)


if __name__ == "__main__":
    print(encode_dashboard(dashboard))
