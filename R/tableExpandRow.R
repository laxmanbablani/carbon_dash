# AUTO GENERATED FILE - DO NOT EDIT

#' @export
tableExpandRow <- function(children=NULL, id=NULL, ariaLabel=NULL, className=NULL, expandHeader=NULL, expandIconDescription=NULL, isExpanded=NULL, isSelected=NULL, loading_state=NULL, onExpand=NULL, style=NULL) {
    
    props <- list(children=children, id=id, ariaLabel=ariaLabel, className=className, expandHeader=expandHeader, expandIconDescription=expandIconDescription, isExpanded=isExpanded, isSelected=isSelected, loading_state=loading_state, onExpand=onExpand, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'TableExpandRow',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'ariaLabel', 'className', 'expandHeader', 'expandIconDescription', 'isExpanded', 'isSelected', 'loading_state', 'onExpand', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
