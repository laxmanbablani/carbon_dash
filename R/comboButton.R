# AUTO GENERATED FILE - DO NOT EDIT

#' @export
comboButton <- function(children=NULL, id=NULL, className=NULL, disabled=NULL, label=NULL, loading_state=NULL, menuAlignment=NULL, onClick=NULL, size=NULL, style=NULL, tooltipAlignment=NULL, translateWithId=NULL) {
    
    props <- list(children=children, id=id, className=className, disabled=disabled, label=label, loading_state=loading_state, menuAlignment=menuAlignment, onClick=onClick, size=size, style=style, tooltipAlignment=tooltipAlignment, translateWithId=translateWithId)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'ComboButton',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'disabled', 'label', 'loading_state', 'menuAlignment', 'onClick', 'size', 'style', 'tooltipAlignment', 'translateWithId'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
