# AUTO GENERATED FILE - DO NOT EDIT

#' @export
tileGroup <- function(children=NULL, id=NULL, className=NULL, defaultSelected=NULL, disabled=NULL, legend=NULL, loading_state=NULL, name=NULL, onChange=NULL, required=NULL, style=NULL, valueSelected=NULL) {
    
    props <- list(children=children, id=id, className=className, defaultSelected=defaultSelected, disabled=disabled, legend=legend, loading_state=loading_state, name=name, onChange=onChange, required=required, style=style, valueSelected=valueSelected)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'TileGroup',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'defaultSelected', 'disabled', 'legend', 'loading_state', 'name', 'onChange', 'required', 'style', 'valueSelected'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
