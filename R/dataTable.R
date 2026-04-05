# AUTO GENERATED FILE - DO NOT EDIT

#' @export
dataTable <- function(children=NULL, id=NULL, className=NULL, description=NULL, experimentalAutoAlign=NULL, filterRows=NULL, header=NULL, headers=NULL, isSortable=NULL, key=NULL, loading_state=NULL, locale=NULL, overflowMenuOnHover=NULL, radio=NULL, render=NULL, rows=NULL, size=NULL, sortRow=NULL, stickyHeader=NULL, style=NULL, title=NULL, translateWithId=NULL, useStaticWidth=NULL, useZebraStyles=NULL, withExpansion=NULL, withSelection=NULL) {
    
    props <- list(children=children, id=id, className=className, description=description, experimentalAutoAlign=experimentalAutoAlign, filterRows=filterRows, header=header, headers=headers, isSortable=isSortable, key=key, loading_state=loading_state, locale=locale, overflowMenuOnHover=overflowMenuOnHover, radio=radio, render=render, rows=rows, size=size, sortRow=sortRow, stickyHeader=stickyHeader, style=style, title=title, translateWithId=translateWithId, useStaticWidth=useStaticWidth, useZebraStyles=useZebraStyles, withExpansion=withExpansion, withSelection=withSelection)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DataTable',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'description', 'experimentalAutoAlign', 'filterRows', 'header', 'headers', 'isSortable', 'key', 'loading_state', 'locale', 'overflowMenuOnHover', 'radio', 'render', 'rows', 'size', 'sortRow', 'stickyHeader', 'style', 'title', 'translateWithId', 'useStaticWidth', 'useZebraStyles', 'withExpansion', 'withSelection'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
