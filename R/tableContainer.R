# AUTO GENERATED FILE - DO NOT EDIT

#' @export
tableContainer <- function(children=NULL, id=NULL, aiEnabled=NULL, className=NULL, decorator=NULL, description=NULL, loading_state=NULL, stickyHeader=NULL, style=NULL, title=NULL, useStaticWidth=NULL) {
    
    props <- list(children=children, id=id, aiEnabled=aiEnabled, className=className, decorator=decorator, description=description, loading_state=loading_state, stickyHeader=stickyHeader, style=style, title=title, useStaticWidth=useStaticWidth)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'TableContainer',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'aiEnabled', 'className', 'decorator', 'description', 'loading_state', 'stickyHeader', 'style', 'title', 'useStaticWidth'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
