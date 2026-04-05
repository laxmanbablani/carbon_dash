# AUTO GENERATED FILE - DO NOT EDIT

#' @export
accordionItem <- function(children=NULL, id=NULL, className=NULL, disabled=NULL, loading_state=NULL, onClick=NULL, onHeadingClick=NULL, open=NULL, persisted_props=NULL, persistence=NULL, persistence_type=NULL, renderExpando=NULL, renderToggle=NULL, style=NULL, title=NULL) {
    
    props <- list(children=children, id=id, className=className, disabled=disabled, loading_state=loading_state, onClick=onClick, onHeadingClick=onHeadingClick, open=open, persisted_props=persisted_props, persistence=persistence, persistence_type=persistence_type, renderExpando=renderExpando, renderToggle=renderToggle, style=style, title=title)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'AccordionItem',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'disabled', 'loading_state', 'onClick', 'onHeadingClick', 'open', 'persisted_props', 'persistence', 'persistence_type', 'renderExpando', 'renderToggle', 'style', 'title'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
