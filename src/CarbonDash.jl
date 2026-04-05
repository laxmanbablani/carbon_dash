
module CarbonDash
using Dash

const resources_path = realpath(joinpath( @__DIR__, "..", "deps"))
const version = "0.0.1"

include("jl/carbondash.jl")

function __init__()
    DashBase.register_package(
        DashBase.ResourcePkg(
            "carbon_dash",
            resources_path,
            version = version,
            [
                DashBase.Resource(
    relative_package_path = "async-CarbonDash.js",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-CarbonDash.js",
    dynamic = nothing,
    async = :true,
    type = :js
),
DashBase.Resource(
    relative_package_path = "async-CarbonDash.js.map",
    external_url = "https://unpkg.com/carbon_dash@0.0.1/carbon_dash/async-CarbonDash.js.map",
    dynamic = true,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "carbon_dash.min.js",
    external_url = nothing,
    dynamic = nothing,
    async = nothing,
    type = :js
),
DashBase.Resource(
    relative_package_path = "carbon_dash.min.js.map",
    external_url = nothing,
    dynamic = true,
    async = nothing,
    type = :js
)
            ]
        )

    )
end
end
