# AUTO GENERATED FILE - DO NOT EDIT

#' @export
tableRow <- function(children=NULL, id=NULL, ariaLabel=NULL, className=NULL, isExpanded=NULL, isSelected=NULL, loading_state=NULL, onExpand=NULL, style=NULL) {
    
    props <- list(children=children, id=id, ariaLabel=ariaLabel, className=className, isExpanded=isExpanded, isSelected=isSelected, loading_state=loading_state, onExpand=onExpand, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'TableRow',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'ariaLabel', 'className', 'isExpanded', 'isSelected', 'loading_state', 'onExpand', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
