import json

from grafanalib._gen import DashboardEncoder
from grafanalib.core import Dashboard, Graph, Row, Target
from grafanalib.prometheus import PromGraph


dashboard = Dashboard(
    title="grafana-snippets » grafanalib » Graph and PromGraph",
    description="Includes a Graph and a PromGraph panel",
    tags=[
        "example",
        "grafana-toolbox",
    ],
    rows=[
        Row(
            panels=[
                Graph(
                    title="zomg constants",
                    dataSource="prometheus",
                    targets=[
                        Target(expr="1"),
                        Target(expr="2"),
                    ],
                ),
                PromGraph(
                    title="zomg prom",
                    data_source="prometheus",
                    expressions=[
                        ("foo", "1"),
                        ("bar", "2"),
                    ],
                ),
            ]
        ),
    ],
).auto_panel_ids()


def encode_dashboard(dashboard) -> str:
    return json.dumps(dashboard, sort_keys=True, cls=DashboardEncoder)


if __name__ == "__main__":
    print(encode_dashboard(dashboard))
