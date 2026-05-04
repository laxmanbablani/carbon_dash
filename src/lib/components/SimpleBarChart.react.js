import React, { useRef, useEffect } from 'react';
import PropTypes from 'prop-types';
import { SimpleBarChart as CarbonSimpleBarChart } from '@carbon/charts';
import '@carbon/charts/styles.css';

const SimpleBarChart = (props) => {
    const {
        id, setProps,
        className = '', style = {}, loading_state,
        data = [], options = {},
        clickData = null, selectedPoint = null,
    } = props;

    const chartRef = useRef(null);
    const instanceRef = useRef(null);

    useEffect(() => {
        if (!chartRef.current) return;

        if (instanceRef.current) {
            instanceRef.current.destroy();
        }

        const chart = new CarbonSimpleBarChart(chartRef.current, { data, options: { height: '400px', ...options } });

        instanceRef.current = chart;

        chartRef.current.addEventListener('bar-click', (event) => {
            const d = event.detail?.datum || event.detail;
            if (setProps) setProps({ clickData: d, selectedPoint: d });
        });

        return () => {
            if (instanceRef.current) {
                instanceRef.current.destroy();
                instanceRef.current = null;
            }
        };
    }, [data]);

    return (
        <div
            id={id} className={className} style={style}
            data-dash-is-loading={loading_state?.is_loading || undefined}
        >
            <div ref={chartRef} style={{ minHeight: "250px", position: "relative" }} />
        </div>
    );
};

SimpleBarChart.propTypes = {
    id: PropTypes.string, setProps: PropTypes.func,
    className: PropTypes.string, style: PropTypes.object,
    loading_state: PropTypes.shape({ is_loading: PropTypes.bool, prop_name: PropTypes.string, component_name: PropTypes.string }),
    /** Array of data objects with group/value fields */
    data: PropTypes.arrayOf(PropTypes.object),
    /** Chart options (title, axes, height, colors, etc.) */
    options: PropTypes.object,
    /** Data from the last clicked bar */
    clickData: PropTypes.object,
    /** The last selected data point */
    selectedPoint: PropTypes.object,
};

SimpleBarChart.defaultProps = { data: [], options: {}, clickData: null, selectedPoint: null };

export default SimpleBarChart;
