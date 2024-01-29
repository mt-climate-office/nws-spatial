from ast import literal_eval
from jinja2 import Environment, FileSystemLoader, Template
import pandas as pd
from pathlib import Path
import json


def render_single_template(
    template: Template,
    row: pd.Series,
    out_dir: Path = Path("./data/alert_pages"),
    for_county: bool = False,
) -> Path:
    events = [json.loads(x) for x in row["nested"]]
    content = template.render(
        zone_name=row["name"],
        events=events,
        zone_descriptor="County" if for_county else "",
    )
    out_pth = out_dir / f"{row['id']}.html"

    with open(out_pth, "w", encoding="utf-8") as file:
        file.write(content)

    return out_pth


def render_templates(
    latest_alerts: Path | pd.DataFrame = "./data/latest_alerts.csv",
    templates: Path = Path("./templates"),
    out_dir: Path = Path("./data/alert_pages"),
    for_county: bool = False,
):
    environment = Environment(loader=FileSystemLoader(templates))
    template = environment.get_template("wx_warnings.html")

    if isinstance(latest_alerts, Path):
        alerts = pd.read_csv(latest_alerts, converters={"nested": literal_eval})
    else:
        alerts = latest_alerts

    for _, row in alerts.iterrows():
        render_single_template(template, row, out_dir, for_county)
