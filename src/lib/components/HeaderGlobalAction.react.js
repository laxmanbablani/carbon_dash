import React from 'react';
import PropTypes from 'prop-types';
import { HeaderGlobalAction as CarbonComponent } from '@carbon/react';
import { getLoadingState } from '../utils/dash';

const HeaderGlobalAction = (props) => {
    const { id, children, className = '', style = {}, loading_state, n_clicks = 0, ...others } = props;
    const handleClick = () => { if (props.setProps) props.setProps({ n_clicks: n_clicks + 1 }); };
    return (
        <CarbonComponent id={id} className={className} style={style}
            data-dash-is-loading={getLoadingState(loading_state) || undefined}
            onClick={handleClick} {...others}>{children}</CarbonComponent>
    );
};

HeaderGlobalAction.propTypes = {
    id: PropTypes.string, setProps: PropTypes.func, children: PropTypes.node,
    className: PropTypes.string, style: PropTypes.object,
    loading_state: PropTypes.shape({ is_loading: PropTypes.bool, prop_name: PropTypes.string, component_name: PropTypes.string }),
    n_clicks: PropTypes.number,
};

HeaderGlobalAction.defaultProps = { n_clicks: 0 };

export default HeaderGlobalAction;
