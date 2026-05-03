/**
 * Shared Dash utility for Carbon components.
 * Provides the getLoadingState helper and shared PropTypes descriptions.
 */

/**
 * Returns the loading state flag for data-dash-is-loading attribute.
 * @param {object} loading_state - Dash loading state object
 * @returns {boolean|undefined}
 */
export const getLoadingState = (loading_state) => {
    if (loading_state && loading_state.is_loading) {
        return true;
    }
    return undefined;
};
