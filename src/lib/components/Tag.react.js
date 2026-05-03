import React from 'react';
import PropTypes from 'prop-types';
import { Tag as CarbonTag, TagSkeleton as CarbonTagSkeleton } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

const Tag = (props) => {
    const { id, children, className = '', style = {}, loading_state, ...others } = props;

    if (loading_state && loading_state.is_loading) {
        return <CarbonTagSkeleton id={id} className={className} />;
    }

    return (
        <CarbonTag
            id={id} className={className} style={style}
            data-dash-is-loading={getLoadingState(loading_state) || undefined}
            {...others}
        >
            {children}
        </CarbonTag>
    );
};

Tag.propTypes = {
    id: PropTypes.string, setProps: PropTypes.func,
    children: PropTypes.node, className: PropTypes.string, style: PropTypes.object,
    loading_state: PropTypes.shape({ is_loading: PropTypes.bool, prop_name: PropTypes.string, component_name: PropTypes.string }),
    /** Type of tag (determines color) */
    type: PropTypes.oneOf([
        'red', 'magenta', 'purple', 'blue', 'cyan', 'teal', 'green',
        'gray', 'cool-gray', 'warm-gray', 'high-contrast', 'outline',
    ]),
    /** Size */
    size: PropTypes.oneOf(['sm', 'md']),
    /** Whether the tag is disabled */
    disabled: PropTypes.bool,
    /** Filter/tag variant */
    filter: PropTypes.bool,
    /** Callback on remove (for filter tags) */
    onClose: PropTypes.func,
    overflowMenu: PropTypes.node,
};

Tag.defaultProps = { type: 'gray', size: 'md', disabled: false, filter: false };

export default Tag;
