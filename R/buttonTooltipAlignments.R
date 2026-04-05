# AUTO GENERATED FILE - DO NOT EDIT

#' @export
buttonTooltipAlignments <- function(children=NULL, id=NULL, className=NULL, style=NULL) {
    
    props <- list(children=children, id=id, className=className, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'ButtonTooltipAlignments',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
