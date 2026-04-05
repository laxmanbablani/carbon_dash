# AUTO GENERATED FILE - DO NOT EDIT

#' @export
dismissibleTag <- function(children=NULL, id=NULL, className=NULL, decorator=NULL, disabled=NULL, dismissTooltipAlignment=NULL, dismissTooltipLabel=NULL, loading_state=NULL, onClose=NULL, renderIcon=NULL, size=NULL, slug=NULL, style=NULL, tagTitle=NULL, text=NULL, title=NULL, type=NULL) {
    
    props <- list(children=children, id=id, className=className, decorator=decorator, disabled=disabled, dismissTooltipAlignment=dismissTooltipAlignment, dismissTooltipLabel=dismissTooltipLabel, loading_state=loading_state, onClose=onClose, renderIcon=renderIcon, size=size, slug=slug, style=style, tagTitle=tagTitle, text=text, title=title, type=type)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'DismissibleTag',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'decorator', 'disabled', 'dismissTooltipAlignment', 'dismissTooltipLabel', 'loading_state', 'onClose', 'renderIcon', 'size', 'slug', 'style', 'tagTitle', 'text', 'title', 'type'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
