# Fleet Data Portfolio

Projects organized around fleet and connected-vehicle business problems. Each implemented project has its own repository with source code, data preparation, validation, results and reproduction instructions. This repository provides navigation only.

## Current work

| Project | Question and scope | Role / level | Status | Repository |
|---|---|---|---|---|
| **DA-E01** Fuel efficiency and price variance | Which fuel changes reflect consumption, purchase timing, prices or measurement gaps? | Data Analyst / Entry | Implemented; acceptance pending | [Open project](https://github.com/JacobCCMorgan/da-e01-fuel-efficiency-analytics) |

## Explore by business topic

| Topic | Questions covered | Projects |
|---|---|---|
| [Fuel, cost and emissions](themes/fuel-cost-emissions.md) | Fuel efficiency, purchase prices, operating cost and emissions intensity. | 4 |
| [Trips and dispatch](themes/trips-dispatch.md) | Dwell time, arrival uncertainty, operating patterns and constrained dispatch. | 4 |
| [Driver behavior and safety](themes/driver-behavior-safety.md) | Risk calibration, video-event review, coaching and intervention evaluation. | 5 |
| [Vehicle maintenance](themes/maintenance.md) | Diagnostic events, maintenance evidence, early warning and capacity allocation. | 3 |
| [Telemetry and ELD quality](themes/telemetry-eld-quality.md) | Device availability, event validity, missing observations and auditable outputs. | 4 |
| [Data integration and platforms](themes/data-platforms.md) | Ingestion, entity history, shared contracts, recovery and reproducible delivery. | 9 |
| [Customer and support services](themes/customer-support.md) | Product adoption, customer service cost, knowledge retrieval and answer evidence. | 4 |
| [HOS and driver work time](themes/hos-worktime.md) | Rule replay, available hours, violation patterns and task-specific work-time risk. | 3 |
| [Hardware and connectivity](themes/hardware-connectivity.md) | Installation quality, diagnostics, reboot/connection behavior, SIM usage and firmware rollout. | 5 |
| [Insurance and partner services](themes/insurance.md) | Exposure history, claims modeling, partner delivery and service-value evaluation. | 3 |
| [Sales and subscription revenue](themes/revenue.md) | Conversion, billing reconciliation, recurring revenue and renewal risk. | 3 |

## How to read the portfolio

- **Released / Accepted:** a versioned implementation and its evidence are available in the linked repository.
- **Implemented; acceptance pending:** the implementation is available at its verified repository link; final review remains open.
- **In progress:** implementation is underway; current results and remaining work are identified in that repository.
- **Planned / Not started:** the question is cataloged; it is not a completed project or a claim of operational impact.
- Project IDs are stable. Role, level and topic describe the intended scope, not a professional credential.

The catalog retains 47 project IDs across 11 business topics. Eight projects form the first implementation batch; the other 39 remain deferred. Work advances one complete project at a time.

## Reuse and data boundaries

Data provenance, permitted uses and limitations are documented in each project. Synthetic demonstrations test explicitly designed scenarios; their results are not presented as measured customer or company savings.

The index does not host production customer data, credentials or duplicate copies of project implementations.

## Maintain the index

Edit `project_catalog.json`, preserve Project IDs, and run `python scripts/build_index.py`. Add a repository URL only after the repository exists and its access has been verified.

[中文導覽](README.zh-TW.md)
