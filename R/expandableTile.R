# AUTO GENERATED FILE - DO NOT EDIT

#' @export
expandableTile <- function(children=NULL, id=NULL, className=NULL, decorator=NULL, expanded=NULL, hasRoundedCorners=NULL, light=NULL, loading_state=NULL, onClick=NULL, onKeyUp=NULL, slug=NULL, style=NULL, tabIndex=NULL, tileCollapsedIconText=NULL, tileCollapsedLabel=NULL, tileExpandedIconText=NULL, tileExpandedLabel=NULL) {
    
    props <- list(children=children, id=id, className=className, decorator=decorator, expanded=expanded, hasRoundedCorners=hasRoundedCorners, light=light, loading_state=loading_state, onClick=onClick, onKeyUp=onKeyUp, slug=slug, style=style, tabIndex=tabIndex, tileCollapsedIconText=tileCollapsedIconText, tileCollapsedLabel=tileCollapsedLabel, tileExpandedIconText=tileExpandedIconText, tileExpandedLabel=tileExpandedLabel)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'ExpandableTile',
        namespace = 'carbon_dash',
        propNames = c('children', 'id', 'className', 'decorator', 'expanded', 'hasRoundedCorners', 'light', 'loading_state', 'onClick', 'onKeyUp', 'slug', 'style', 'tabIndex', 'tileCollapsedIconText', 'tileCollapsedLabel', 'tileExpandedIconText', 'tileExpandedLabel'),
        package = 'carbonDash'
        )

    structure(component, class = c('dash_component', 'list'))
}
