# AUTO GENERATED FILE - DO NOT EDIT

#' @export
tableCell <- function(children=NULL, id=NULL, className=NULL, colSpan=NULL, hasAILabelHeader=NULL, headers=NULL, loading_state=NULL, style=NULL) {
    
    props <- list(children=children, id=id, className=className, colSpan=colSpan, hasAILabelHeader=hasAILabelHeader, headers=headers, loading_state=loading_state, style=style)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'TableCell',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'colSpan', 'hasAILabelHeader', 'headers', 'loading_state', 'style'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
