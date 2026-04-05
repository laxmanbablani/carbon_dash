# AUTO GENERATED FILE - DO NOT EDIT

#' @export
table <- function(children=NULL, id=NULL, className=NULL, experimentalAutoAlign=NULL, isSortable=NULL, loading_state=NULL, overflowMenuOnHover=NULL, size=NULL, stickyHeader=NULL, style=NULL, tabIndex=NULL, useStaticWidth=NULL, useZebraStyles=NULL) {
    
    props <- list(children=children, id=id, className=className, experimentalAutoAlign=experimentalAutoAlign, isSortable=isSortable, loading_state=loading_state, overflowMenuOnHover=overflowMenuOnHover, size=size, stickyHeader=stickyHeader, style=style, tabIndex=tabIndex, useStaticWidth=useStaticWidth, useZebraStyles=useZebraStyles)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'Table',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'experimentalAutoAlign', 'isSortable', 'loading_state', 'overflowMenuOnHover', 'size', 'stickyHeader', 'style', 'tabIndex', 'useStaticWidth', 'useZebraStyles'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
