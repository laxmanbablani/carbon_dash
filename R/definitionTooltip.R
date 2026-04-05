# AUTO GENERATED FILE - DO NOT EDIT

#' @export
definitionTooltip <- function(children=NULL, id=NULL, align=NULL, autoAlign=NULL, className=NULL, defaultOpen=NULL, definition=NULL, loading_state=NULL, openOnHover=NULL, style=NULL, tooltipText=NULL, triggerClassName=NULL) {
    
    props <- list(children=children, id=id, align=align, autoAlign=autoAlign, className=className, defaultOpen=defaultOpen, definition=definition, loading_state=loading_state, openOnHover=openOnHover, style=style, tooltipText=tooltipText, triggerClassName=triggerClassName)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DefinitionTooltip',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'align', 'autoAlign', 'className', 'defaultOpen', 'definition', 'loading_state', 'openOnHover', 'style', 'tooltipText', 'triggerClassName'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
