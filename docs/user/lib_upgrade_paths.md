# Upgrade Paths

The `UPGRADE_PATHS` definition in constants is maintained based on the following rules:

* They are not considered vendor recommendations, instead an interpretation based on the open source contributor.
* There is no expectation they will be updated, as such issues requesting updates will be closed but PRs to update--following the below rules--will be accepted.
* The lists can only be modified by added to during any patch or minor version.
* The list cannot be modified in any other way.
* Generate a new versioned list, e.g. PANOS_OFFICIAL_V2 vs PANOS_OFFICIAL_V1 and create an alternate list.
* During major version changes (e.g. 1.x.x to 2.x.x) lists may be removed.
