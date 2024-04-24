from grafana_dashboard.manual_models import TimeSeries
from grafana_dashboard.model.dashboard_types_gen import Dashboard, GridPos
from grafana_dashboard.model.prometheusdataquery_types_gen import PrometheusDataQuery

dashboard = Dashboard(
    title="grafana-snippets » grafana-dashboard » Prometheus Time Series",
    description="Includes a time series panel, using a Prometheus query",
    tags=[
        "example",
        "grafana-toolbox",
        "play.grafana.org",
    ],
    panels=[
        TimeSeries(
            title="Panel Title",
            gridPos=GridPos(x=0, y=0, w=12, h=9),
            targets=[
                PrometheusDataQuery(
                    datasource="Prometheus",
                    expr='avg(1 - rate(node_cpu_seconds_total{mode="idle"}[$__rate_interval])) by (instance, job)',
                    legendFormat="{{instance}}",
                )
            ],
        )
    ],
).auto_panel_ids()


if __name__ == "__main__":
    print(dashboard.to_grafana_json())
