"""Selected, source-backed evidence for the project detail dashboards."""
import streamlit as st


def render_selected_evidence(project):
    evidence = project.get('evidence', {})
    project_id = project['id']
    if project_id == 'readmission':
        st.subheader('Validation model comparison')
        rows = []
        for model in evidence['VALIDATION_MODELS']:
            rows.append({
                'Model': model['Model'],
                'Accuracy': f"{model['Accuracy']:.2%}",
                'Macro F1': f"{model['Macro F1']:.2%}",
                'Within-30-day recall': f"{model['Within 30 recall']:.2%}",
                'Log loss': model['Log loss'],
            })
        st.dataframe(rows, hide_index=True, use_container_width=True)
        st.caption('Validation results used for model selection; these are separate from the frozen test results above. The two-stage model has higher accuracy but much lower early-readmission recall. The 60/40 ensemble has the highest macro F1 among these candidates.')

        features, calibration = st.columns(2, gap='large')
        with features:
            st.subheader('Leading model features')
            records = [{'Feature': name.replace('_', ' '), 'Importance': value} for name, value in evidence['FEATURE_IMPORTANCE'][:8]]
            st.vega_lite_chart({
                'data': {'values': records}, 'height': 280,
                'mark': {'type': 'bar', 'color': '#8bd3ad', 'cornerRadiusEnd': 4},
                'encoding': {
                    'y': {'field': 'Feature', 'type': 'nominal', 'sort': '-x', 'axis': {'title': None, 'labelLimit': 200}},
                    'x': {'field': 'Importance', 'type': 'quantitative', 'axis': {'title': 'Reported importance'}},
                    'tooltip': [{'field': 'Feature'}, {'field': 'Importance', 'format': '.2f'}],
                }, 'config': {'view': {'stroke': None}},
            }, use_container_width=True)
            st.caption('Top eight importance values from the published benchmark. Importance describes model reliance, not causal effects or clinical recommendations.')
        with calibration:
            st.subheader('Probability calibration')
            rows = [{
                'Outcome': row['Class'],
                'Observed rate': f"{row['Observed']:.2%}",
                'Mean before': f"{row['Mean before']:.2%}",
                'Mean after': f"{row['Mean after']:.2%}",
                'Brier before': row['Brier before'],
                'Brier after': row['Brier after'],
            } for row in evidence['CALIBRATION']]
            st.dataframe(rows, hide_index=True, use_container_width=True)
            st.caption('Published calibration summary. Lower Brier scores indicate better probability accuracy. Calibrated probabilities are exploratory; the frozen class decisions use uncalibrated ensemble probabilities.')
        st.markdown('[Evidence: published benchmark](https://github.com/PriyankaRauniyar/Hospital-readmission-risk-dashboard/blob/main/benchmark.py)')
    elif project_id == 'pantrypulse':
        st.subheader('Forecast backtest vs a simple baseline')
        st.dataframe(evidence['backtest'], hide_index=True, use_container_width=True)
        st.caption('Unweighted county averages from the published 12-week holdout export. MAPE is mean absolute percentage error; lower is better. Range coverage is the percentage of simulated holdout observations inside the forecast interval. This measures performance on simulated weekly visits, not real-world forecast accuracy.')
        st.subheader('Dallas County · eight-week planning outlook')
        st.dataframe(evidence['forecast'], hide_index=True, use_container_width=True)
        st.caption('Published September 2026 snapshot. Compare the upper forecast bound with simulated capacity to understand alert status; this table is not a live feed.')
        st.markdown('[Backtest source](https://github.com/PriyankaRauniyar/PantryPulse-Food-Insecurity-Analytics-and-Forecasting/blob/main/outputs/backtest_accuracy.csv) · [Forecast source](https://github.com/PriyankaRauniyar/PantryPulse-Food-Insecurity-Analytics-and-Forecasting/blob/main/outputs/forecast_with_alerts.csv)')
    elif project_id in ('learning-platform', 'emergency-room'):
        st.subheader('Key entities & relationships')
        st.dataframe(evidence['schema'], hide_index=True, use_container_width=True)
        if project_id == 'learning-platform':
            st.caption('Selected relationships from the published SQL: users connect to roles; courses connect to creators and categories; enrollment, assessment, payment, and certificate records connect learners to courses.')
        else:
            st.caption('Selected relationships from the published SQL: admissions connect patients to shifts and staff; bed assignments preserve assignment times; supervision and medication administration connect care activity to staff and shifts.')
        st.caption('This table explains the relational data model. It summarizes schema definitions, rather than executed query results.')
        link = next(link for link in project['links'] if 'SQL' in link['label'])
        st.markdown(f"[Evidence: published SQL schema]({link['url']})")
