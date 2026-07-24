---
source_url: https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/wsff.md
ingested: 2026-07-23
sha256: 1d26f46641214b8954834a38b84a721f31cf8c952c18e22d7266c9f9eea0d576
blog_source: Hacker News
---




  

<!DOCTYPE html>
<html
  lang="en"
  
  data-color-mode="auto" data-light-theme="light" data-dark-theme="dark"
  data-a11y-animated-images="system" data-a11y-link-underlines="true"
  
  >




  <head>
    <meta charset="utf-8">
  <link rel="dns-prefetch" href="https://github.githubassets.com">
  <link rel="dns-prefetch" href="https://avatars.githubusercontent.com">
  <link rel="dns-prefetch" href="https://github-cloud.s3.amazonaws.com">
  <link rel="dns-prefetch" href="https://user-images.githubusercontent.com/">
  <link rel="preconnect" href="https://github.githubassets.com" crossorigin>
  <link rel="preconnect" href="https://avatars.githubusercontent.com">

  


  <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/light-62b06818b06b09b7.css" /><link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/light_high_contrast-44cd405df9340c5c.css" /><link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/dark-f3311053b052c5d4.css" /><link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/dark_high_contrast-6739a26cef6aaf8e.css" /><link data-color-theme="light" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light-62b06818b06b09b7.css" /><link data-color-theme="light_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_high_contrast-44cd405df9340c5c.css" /><link data-color-theme="light_colorblind" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_colorblind-646991fe4831aa4c.css" /><link data-color-theme="light_colorblind_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_colorblind_high_contrast-4a10ec40fc7845a6.css" /><link data-color-theme="light_tritanopia" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_tritanopia-ad55fa69f5aaa75d.css" /><link data-color-theme="light_tritanopia_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/light_tritanopia_high_contrast-eed7315d90377f7a.css" /><link data-color-theme="dark" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark-f3311053b052c5d4.css" /><link data-color-theme="dark_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_high_contrast-6739a26cef6aaf8e.css" /><link data-color-theme="dark_colorblind" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_colorblind-46654068ac8d8b19.css" /><link data-color-theme="dark_colorblind_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_colorblind_high_contrast-ce6091c5adfeb70f.css" /><link data-color-theme="dark_tritanopia" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_tritanopia-a1584556afb3c856.css" /><link data-color-theme="dark_tritanopia_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_tritanopia_high_contrast-f48b2521c34c41b6.css" /><link data-color-theme="dark_dimmed" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_dimmed-6199d2c64677af2d.css" /><link data-color-theme="dark_dimmed_high_contrast" crossorigin="anonymous" media="all" rel="stylesheet" data-href="https://github.githubassets.com/assets/dark_dimmed_high_contrast-a8e662a03107fa71.css" />

  <style type="text/css">
    :root {
      --tab-size-preference: 4;
    }

    pre, code {
      tab-size: var(--tab-size-preference);
    }
  </style>

    <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/primer-primitives-ac2f4b33720c6312.css" />
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/primer-bb3e7caff8347285.css" />
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/global-1832d803adebd2b4.css" />
    <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/github-cf976967feea1e66.css" />
  <link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/repository-6534fbc3f5e83ac0.css" />
<link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/code-a5d20170108e1057.css" />

  

  <script type="application/json" id="client-env">{"locale":"en","featureFlags":["actions_enable_background_steps","activity_diff_file_tree","activity_repos_file_tree","activity_repos_overview_header","activity_repos_overview_sidebar","agent_author_search_expansion","agent_author_search_expansion_ui_pulls","alternate_user_config_repo","artifact_ui_v2","billing_billable_licenses_cost_center_bucket_fix","billing_cost_center_user_level_budgets","billing_discount_threshold_notification","billing_multi_user_cost_center_total_user_count","billing_user_level_budgets","billing_user_level_budgets_manage","ccr_files_changed_model_picker","code_quality_ccr","code_quality_enablement_banner_targeting","code_quality_new_repo_selection_card","code_quality_remove_preview","code_view_raf_sticky_lines","codespaces_prebuild_region_target_update","coding_agent_third_party_model_ui","comment_viewer_copy_raw_markdown","contentful_primer_code_blocks","copilot_agent_snippy","copilot_api_agentic_issue_marshal_yaml","copilot_ask_mode_dropdown","copilot_automations_pagination","copilot_chat_attach_multiple_images","copilot_chat_auto_mode_picker_paid","copilot_chat_category_rate_limit_messages","copilot_chat_clear_model_selection_for_default_change","copilot_chat_compact_tables","copilot_chat_docked_panel","copilot_chat_enable_tool_call_logs","copilot_chat_header_reorder","copilot_chat_input_commands","copilot_chat_interspersed_tool_calls","copilot_chat_max_upsell","copilot_chat_model_picker_promotions","copilot_chat_models_browser_cache","copilot_chat_opening_thread_switch","copilot_chat_per_message_token_usage","copilot_chat_prettify_pasted_code","copilot_chat_reduce_quota_checks","copilot_chat_ubb_meter","copilot_chat_vision_dotcom_chat_ga_gate","copilot_chat_vision_in_claude","copilot_chat_vision_preview_gate","copilot_cli_install_cta_max_plan","copilot_css_textarea_autosize","copilot_custom_copilots","copilot_custom_copilots_feature_preview","copilot_diff_explain_conversation_intent","copilot_diff_reference_context","copilot_duplicate_thread","copilot_extensions_removal_on_marketplace","copilot_file_block_ref_matching","copilot_fix_failed_workflows_all_skus","copilot_ftp_hyperspace_upgrade_prompt","copilot_hide_hovercard","copilot_immersive_code_block_transition_wrap","copilot_immersive_embedded_deferred_payload","copilot_immersive_embedded_draggable","copilot_immersive_embedded_header_button","copilot_immersive_embedded_implicit_references","copilot_immersive_embedded_skip_copilot_api_token_for_dotcom_context","copilot_immersive_file_block_transition_open","copilot_immersive_file_preview_keep_mounted","copilot_immersive_job_result_preview","copilot_immersive_suggestion_pills","copilot_immersive_task_hyperlinking","copilot_immersive_task_within_chat_thread","copilot_mc_cli_resume_any_users_task","copilot_mc_nudges","copilot_mission_control_agent_filtering","copilot_mission_control_environment_list_icons","copilot_mission_control_needs_attention","copilot_mission_control_sandbox_remote_bypass","copilot_mission_control_session_events_ui","copilot_mission_control_session_filters","copilot_mission_control_task_alive_updates","copilot_mission_control_task_sharing","copilot_org_policy_page_focus_mode","copilot_plans_signups_enabled","copilot_pr_chat_enhancements","copilot_prominent_upgrade_button","copilot_redirect_header_button_to_agents","copilot_resource_panel","copilot_share_active_subthread","copilot_spaces_ga","copilot_spaces_individual_policies_ga","copilot_spark_empty_state","copilot_spark_handle_nil_friendly_name","copilot_swe_agent_authorization_status_ui","copilot_swe_agent_hide_model_picker_if_only_auto","copilot_swe_agent_issue_comment_trigger","copilot_swe_agent_pr_comment_model_picker","copilot_swe_agent_pull_request_comment_trigger","copilot_swe_agent_pull_request_merged_trigger","copilot_swe_agent_pull_request_opened_trigger","copilot_swe_agent_pull_request_synchronize_trigger","copilot_swe_agent_use_subagents","copilot_task_api_github_rest_style","copilot_token_based_billing","copilot_unconfigured_is_inherited","copilot_user_can_upgrade_plan_field","copilot_workbench_ubb","dashboard_indexeddb_caching","dashboard_lists_max_age_filter","dashboard_surface_persistent_preferences","dashboard_universe_2025_feedback_dialog","flex_cta_groups_mvp","ga_enterprise_teams_ui","global_nav_react","hpc_error_overhead","hyperspace_2025_logged_out_batch_1","hyperspace_2025_logged_out_batch_2","hyperspace_2025_logged_out_batch_3","in_product_messaging_datadog_monitoring","ipm_budget_deep_linking","ipm_global_transactional_message_agents","ipm_global_transactional_message_copilot","ipm_global_transactional_message_issues","ipm_global_transactional_message_prs","ipm_global_transactional_message_repos","ipm_global_transactional_message_spaces","issue_cca_modal_open","issue_cca_multi_assign_modal","issue_cca_visualization","issue_inline_avatars","issue_relative_time_micro","issues_expanded_file_types","issues_lazy_load_comment_box_suggestions","issues_react_chrome_container_query_fix","landing_pages_ninetailed","landing_pages_web_vitals_tracking","lifecycle_label_name_updates","low_quality_classifier","marketing_pages_search_explore_provider","memex_default_issue_create_repository","memex_lazy_hydrate_agent_tasks","memex_live_update_hovercard","memex_mwl_filter_field_delimiter","memex_remove_deprecated_type_issue","merge_status_header_feedback","oauth_authorize_clickjacking_protection","octocaptcha_origin_optimization","primer_react_css_anchor_positioning","property_definition_empty_state_suggestions","prs_copilot_app_open_action","prs_css_anchor_positioning","pull_request_copilot_attribution_header","pull_request_overview_panel_edit_description","react_blob_isolate_code_lines","react_data_router_tanstack_allowed","react_router_external_route_handoff","react_sandbox_future_tanstack","repo_issues_sidebar_layout","repo_overview_ask_copilot","repos_contributors_limited_default_range","review_involves_filter","sample_network_conn_type","secret_scanning_pattern_alerts_link","security_center_artifact_filters_popover","semantic_similarity_duplicate_issue_detection","session_logs_ungroup_reasoning_text","site_banner_desktop_copilot_app","site_code_quality_page","site_github_app_ga_page","site_global_banner_learn_copilot_app","site_global_banner_security_webinar","site_global_nav_spark_models_removed","spark_prompt_secret_scanning","spark_server_connection_status","suppress_automated_browser_vitals","swp_forms_disable_octocaptcha","update_issue_suggestions","viewscreen_sandbox","warn_inaccessible_attachments","webp_support","workbench_store_readonly","rspack_esm_output","rspack_esm_output"],"copilotApiOverrideUrl":"https://api.githubcopilot.com","cmcApiUrl":"https://api.github.com/cmc_internal/api"}</script>
<script crossorigin="anonymous" type="module" src="https://github.githubassets.com/assets/high-contrast-cookie-9d73b8ae1abef9dc.js"></script>
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/wp-runtime-652a51fe8b67a946.js" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/app-foundation-3d8531a467106c35.js" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/app-runtime-96b6841ae9810d0a.js" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/fetch-utilities-c15f4a0ba1130fd4.js" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/78205-77cb95bbaf5d2f94.js" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/89415-f37fe7ab0182fc38.js" />
<script crossorigin="anonymous" type="module" src="https://github.githubassets.com/assets/environment-60e3817e48f44e07.js" defer="defer"></script>
<link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/app-runtime.180e5b7308d67ecf.module.css" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/catalyst-03fc2ee1b163e4cb.js" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/selector-observer-31e911ea8e9046d3.js" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/relative-time-element-dfbe05d051d2745a.js" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/296-cddf2922ea3a416c.js" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/816-29b762091e5033a9.js" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/65637-e357a8be37eda955.js" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/31721-903cd2b317a8cc03.js" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/46740-0a6e4901e467cc61.js" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/91445-6f5c449d48bb47ab.js" />
<script crossorigin="anonymous" type="module" src="https://github.githubassets.com/assets/github-elements-d33eb15cc9d5e4ed.js" defer="defer"></script>
<script crossorigin="anonymous" type="module" src="https://github.githubassets.com/assets/element-registry-8799a34369c15d03.js" defer="defer"></script>
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/runtime-helpers-b5a5a1cee32a4b87.js" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/aria-live-f89426702b2d1650.js" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/hotkey-18e2cf4c6aadb3ff.js" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/react-core-8f487d18753bf3b6.js" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/react-lib-a79e0802ead09943.js" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/38566-0e2fc1e26fe33e26.js" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/79039-9238f8fd47d74629.js" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/88475-e7c45daacb58e0a3.js" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/26533-557f05825ff30790.js" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/3609-2a17d1c3e2ce7fe5.js" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/74809-4df83b7c30013f54.js" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/40489-1cb4158300f5cf11.js" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/85720-fc27301ab71403cf.js" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/6059-001e1b0cb00e4a0b.js" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/29863-48ad2609b0f83022.js" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/27956-409bb692f2b6523b.js" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/24061-55c5ea4be30ab4b5.js" />
<script crossorigin="anonymous" type="module" src="https://github.githubassets.com/assets/behaviors-cd55a3655b828125.js" defer="defer"></script>
<link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/react-core.893b53f4d8f6405e.module.css" />
<script crossorigin="anonymous" type="module" src="https://github.githubassets.com/assets/code-menu-fdd4ad594fe89f46.js" defer="defer"></script>
  
  <link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/primer-react-1fcafbe41909a6b8.js" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/octicons-react-0f7aabd2961515ac.js" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/65063-b4693aba6fc1af8e.js" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/437-e211f0d3b29f548a.js" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/53351-c7a0796f923dc77c.js" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/7463-886fbf7975c0e6d4.js" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/27600-ca5896d422c7dee2.js" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/88493-eabaae5d94674ff7.js" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/47406-7666df4c77b449d9.js" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/76041-6118fbdcc7fd198e.js" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/27784-0cb7688f5c662c21.js" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/99829-93eab990d668cd70.js" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/71192-87b68d371daccae0.js" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/4871-d4c66be5b6789608.js" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/57664-4be11172b1253f5b.js" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/56324-fdc822b960b89999.js" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/4706-4d3c62464fbdd35d.js" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/47278-5bde9117e40f98de.js" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/10257-a73e531345938203.js" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/1966-7fbeda16787b1887.js" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/8151-9fc11fb2f79e768d.js" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/11494-ffe52f81d15e7ba9.js" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/13735-b98e51f0f3d35f17.js" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/99788-02d0a8f5e37ae567.js" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/30223-4036f6c2f2c51cf3.js" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/21472-ed8c6f1b49257b4b.js" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/79589-17143cd2888989ae.js" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/24860-70121da41a4fb7f5.js" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/85736-8a75fdce27024c9a.js" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/32146-6a3e09dd9befa69a.js" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/4889-37caaa6be8e29ac3.js" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/54050-d9d79abd130eb040.js" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/13199-e907ddb92cd44a5f.js" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/66917-60b4817426fb28cb.js" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/3399-54982322f008eb6b.js" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/26473-70e5bfe231559bcf.js" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/4409-4e086be10fa58ee4.js" />
<script crossorigin="anonymous" type="module" src="https://github.githubassets.com/assets/code-view-4e0170f934200835.js" defer="defer"></script>
<link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/primer-react-css.ba5192c6c34cad29.module.css" />
<link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/99788.99e8d1df230f15ac.module.css" />
<link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/4409.0fbffcfe206d6892.module.css" />
<link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/code-view.efaef522425547ac.module.css" />

  <link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/93986-f6551bbe82278926.js" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/22415-9cf896eee804de12.js" />
<script crossorigin="anonymous" type="module" src="https://github.githubassets.com/assets/notifications-subscriptions-menu-6eea097f45c146ab.js" defer="defer"></script>
<link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/primer-react-css.ba5192c6c34cad29.module.css" />
<link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/notifications-subscriptions-menu.1de098383f2ca165.module.css" />


  <title>advanced-context-engineering-for-coding-agents/wsff.md at main · humanlayer/advanced-context-engineering-for-coding-agents · GitHub</title>



  <meta name="route-pattern" content="/:user_id/:repository/blob/*name(/*path)" data-turbo-transient>
  <meta name="route-controller" content="blob" data-turbo-transient>
  <meta name="route-action" content="show" data-turbo-transient>
  <meta name="fetch-nonce" content="v2:c51627c3-3efa-92d2-2351-bc99c611de25">

    
  <meta name="current-catalog-service-hash" content="f3abb0cc802f3d7b95fc8762b94bdcb13bf39634c40c357301c4aa1d67a256fb">


  <meta name="request-id" content="F26E:36B65A:24E9B91:1D57819:6A62591C" data-pjax-transient="true"/><meta name="html-safe-nonce" content="37e4f9b5a9afaa6b907ee997b9533ea014f265314140efbf369b11a3f24face3" data-pjax-transient="true"/><meta name="visitor-payload" content="eyJyZWZlcnJlciI6IiIsInJlcXVlc3RfaWQiOiJGMjZFOjM2QjY1QToyNEU5QjkxOjFENTc4MTk6NkE2MjU5MUMiLCJ2aXNpdG9yX2lkIjoiNzUzNDQ3NTQ0OTEzMTQ4OTU2NCIsInJlZ2lvbl9lZGdlIjoiZnJhIiwicmVnaW9uX3JlbmRlciI6ImZyYSJ9" data-pjax-transient="true"/><meta name="visitor-hmac" content="6561a1d048815e4ac13dbbd21c01a081210c01761cecb53ba2e7e55ae0ef846f" data-pjax-transient="true"/>


    <meta name="hovercard-subject-tag" content="repository:1047081321" data-turbo-transient>


  <meta name="github-keyboard-shortcuts" content="repository,source-code,file-tree,copilot" data-turbo-transient="true" />
  

  <meta name="selected-link" value="repo_source" data-turbo-transient>
  <link rel="assets" href="https://github.githubassets.com/">

    <meta name="google-site-verification" content="Apib7-x98H0j5cPqHWwSMm6dNU4GmODRoqxLiDzdx9I">

<meta name="octolytics-url" content="https://collector.github.com/github/collect" />





  <meta name="analytics-location" content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-turbo-transient="true" />

  




    <meta name="user-login" content="">

  

    <meta name="viewport" content="width=device-width">

    

      <meta name="description" content="Contribute to humanlayer/advanced-context-engineering-for-coding-agents development by creating an account on GitHub.">

      <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">

    <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
    <meta property="fb:app_id" content="1401488693436528">
    <meta name="apple-itunes-app" content="app-id=1477376905, app-argument=https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/wsff.md" />

      <meta name="twitter:image" content="https://opengraph.githubassets.com/3276d916ee0592f9fc50dbcf0de49f98f9b5796862da7af049acb790627520c9/humanlayer/advanced-context-engineering-for-coding-agents" /><meta name="twitter:site" content="@github" /><meta name="twitter:card" content="summary_large_image" /><meta name="twitter:title" content="advanced-context-engineering-for-coding-agents/wsff.md at main · humanlayer/advanced-context-engineering-for-coding-agents" /><meta name="twitter:description" content="Contribute to humanlayer/advanced-context-engineering-for-coding-agents development by creating an account on GitHub." />
  <meta property="og:image" content="https://opengraph.githubassets.com/3276d916ee0592f9fc50dbcf0de49f98f9b5796862da7af049acb790627520c9/humanlayer/advanced-context-engineering-for-coding-agents" /><meta property="og:image:alt" content="Contribute to humanlayer/advanced-context-engineering-for-coding-agents development by creating an account on GitHub." /><meta property="og:image:width" content="1200" /><meta property="og:image:height" content="600" /><meta property="og:site_name" content="GitHub" /><meta property="og:type" content="object" /><meta property="og:title" content="advanced-context-engineering-for-coding-agents/wsff.md at main · humanlayer/advanced-context-engineering-for-coding-agents" /><meta property="og:url" content="https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/wsff.md" /><meta property="og:description" content="Contribute to humanlayer/advanced-context-engineering-for-coding-agents development by creating an account on GitHub." />
  




      <meta name="hostname" content="github.com">



        <meta name="expected-hostname" content="github.com">


  <meta http-equiv="x-pjax-version" content="89f98d29df9690bf0d597745219ec2cfcd5e45b4d324b6866b6b5f89ff964fcb" data-turbo-track="reload">
  <meta http-equiv="x-pjax-csp-version" content="cb4cffb7c023f774818cf728eb860debf1fc8ecf88a20487b238da276df1eb7d" data-turbo-track="reload">
  <meta http-equiv="x-pjax-css-version" content="0f66651d491e0bc927f9973a3bded16a7dcf41eb68077453352dc15547622c59" data-turbo-track="reload">
  <meta http-equiv="x-pjax-js-version" content="b928dd27bb9305f313c737471c216297e218430ec505d064cf33d7d74af9bf89" data-turbo-track="reload">

  <meta name="turbo-cache-control" content="no-preview" data-turbo-transient="">

      <meta name="turbo-cache-control" content="no-cache" data-turbo-transient>

    <meta data-hydrostats="publish">

  <meta name="go-import" content="github.com/humanlayer/advanced-context-engineering-for-coding-agents git https://github.com/humanlayer/advanced-context-engineering-for-coding-agents.git">

  <meta name="octolytics-dimension-user_id" content="177409041" /><meta name="octolytics-dimension-user_login" content="humanlayer" /><meta name="octolytics-dimension-repository_id" content="1047081321" /><meta name="octolytics-dimension-repository_nwo" content="humanlayer/advanced-context-engineering-for-coding-agents" /><meta name="octolytics-dimension-repository_public" content="true" /><meta name="octolytics-dimension-repository_is_fork" content="false" /><meta name="octolytics-dimension-repository_network_root_id" content="1047081321" /><meta name="octolytics-dimension-repository_network_root_nwo" content="humanlayer/advanced-context-engineering-for-coding-agents" />
  



    

    <meta name="turbo-body-classes" content="logged-out env-production page-responsive">
  <meta name="disable-turbo" content="false">


  <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">


  <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">

    <meta name="release" content="6f728c3f39985ee4d171ffdd5591d8d2652392d9" data-turbo-track="reload">
  <meta name="ui-target" content="full">

  <link rel="mask-icon" href="https://github.githubassets.com/assets/pinned-octocat-093da3e6fa40.svg" color="#000000">
  <link rel="alternate icon" class="js-site-favicon" type="image/png" href="https://github.githubassets.com/favicons/favicon.png">
  <link rel="icon" class="js-site-favicon" type="image/svg+xml" href="https://github.githubassets.com/favicons/favicon.svg" data-base-href="https://github.githubassets.com/favicons/favicon">

<meta name="theme-color" content="#1e2327">
<meta name="color-scheme" content="light dark" />


  <link rel="manifest" href="/manifest.json" crossOrigin="use-credentials">

  </head>

  <body class="logged-out env-production page-responsive" style="word-wrap: break-word;" >
    <div data-turbo-body class="logged-out env-production page-responsive" style="word-wrap: break-word;" >
      <div id="__primerPortalRoot__" style="z-index: 1000; position: absolute; width: 100%;" data-turbo-permanent></div>
      

    <div class="position-relative header-wrapper js-header-wrapper ">
      <a href="#start-of-content" data-skip-target-assigned="false" class="px-2 tmp-py-4 color-bg-accent-emphasis color-fg-on-emphasis show-on-focus js-skip-to-content">Skip to content</a>

      <span data-view-component="true" class="progress-pjax-loader Progress position-fixed width-full">
    <span style="width: 0%;" data-view-component="true" class="Progress-item progress-pjax-loader-bar left-0 top-0 color-bg-accent-emphasis"></span>
</span>      
      <link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/94189-1eee5e7ebafbb892.js" fetchpriority="low" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/keyboard-shortcuts-dialog-4c01333f69439482.js" fetchpriority="low" />
<link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/primer-react-css.ba5192c6c34cad29.module.css" />
<link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/keyboard-shortcuts-dialog.2c7bec7e356dcc37.module.css" />

<react-partial
  partial-name="keyboard-shortcuts-dialog"
  data-ssr="false"
  data-attempted-ssr="false"
  data-react-profiling="false"
>
  
  <script type="application/json" data-target="react-partial.embeddedData">{"props":{"docsUrl":"https://docs.github.com/get-started/accessibility/keyboard-shortcuts"}}</script>
  <div data-target="react-partial.reactRoot"></div>
</react-partial>





      

          

              
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/70666-774087b76d27f9f3.js" />
<script crossorigin="anonymous" type="module" src="https://github.githubassets.com/assets/sessions-36c5bead84e8b9fe.js" defer="defer"></script>

<style>
  /* Override primer focus outline color for marketing header dropdown links for better contrast */
  [data-color-mode="light"] .HeaderMenu-dropdown-link:focus-visible,
  [data-color-mode="light"] .HeaderMenu-trailing-link a:focus-visible {
    outline-color: var(--color-accent-fg);
  }
</style>

<header class="HeaderMktg header-logged-out js-details-container js-header Details f4 tmp-py-3" role="banner" data-is-top="true" data-color-mode=auto data-light-theme=light data-dark-theme=dark>
  <h2 class="sr-only">Navigation Menu</h2>

  <button type="button" class="HeaderMktg-backdrop d-lg-none border-0 position-fixed top-0 left-0 width-full height-full js-details-target" aria-label="Toggle navigation">
    <span class="d-none">Toggle navigation</span>
  </button>

  <div class="d-flex flex-column flex-lg-row flex-items-center tmp-px-3 tmp-px-md-4 tmp-px-lg-5 height-full position-relative z-1">
    <div class="d-flex flex-justify-between flex-items-center width-full width-lg-auto">
      <div class="flex-1">
        <button aria-label="Toggle navigation" aria-expanded="false" type="button" data-view-component="true" class="js-details-target js-nav-padding-recalculate js-header-menu-toggle Button--link Button--medium Button d-lg-none color-fg-inherit p-1 tmp-p-1">  <span class="Button-content">
    <span class="Button-label"><div class="HeaderMenu-toggle-bar rounded my-1"></div>
            <div class="HeaderMenu-toggle-bar rounded my-1"></div>
            <div class="HeaderMenu-toggle-bar rounded my-1"></div></span>
  </span>
</button>
      </div>

      <a class="tmp-mr-lg-3 color-fg-inherit flex-order-2 js-prevent-focus-on-mobile-nav"
        href="/"
        aria-label="Homepage"
        data-analytics-event="{&quot;category&quot;:&quot;Marketing nav&quot;,&quot;action&quot;:&quot;click to go to homepage&quot;,&quot;label&quot;:&quot;ref_page:Marketing;ref_cta:Logomark;ref_loc:Header&quot;}">
        <svg height="32" aria-hidden="true" data-component="Octicon" viewBox="0 0 24 24" version="1.1" width="32" data-view-component="true" class="octicon octicon-mark-github">
    <path d="M10.226 17.284c-2.965-.36-5.054-2.493-5.054-5.256 0-1.123.404-2.336 1.078-3.144-.292-.741-.247-2.314.09-2.965.898-.112 2.111.36 2.83 1.01.853-.269 1.752-.404 2.853-.404 1.1 0 1.999.135 2.807.382.696-.629 1.932-1.1 2.83-.988.315.606.36 2.179.067 2.942.72.854 1.101 2 1.101 3.167 0 2.763-2.089 4.852-5.098 5.234.763.494 1.28 1.572 1.28 2.807v2.336c0 .674.561 1.056 1.235.786 4.066-1.55 7.255-5.615 7.255-10.646C23.5 6.188 18.334 1 11.978 1 5.62 1 .5 6.188.5 12.545c0 4.986 3.167 9.12 7.435 10.669.606.225 1.19-.18 1.19-.786V20.63a2.9 2.9 0 0 1-1.078.224c-1.483 0-2.359-.808-2.987-2.313-.247-.607-.517-.966-1.034-1.033-.27-.023-.359-.135-.359-.27 0-.27.45-.471.898-.471.652 0 1.213.404 1.797 1.235.45.651.921.943 1.483.943.561 0 .92-.202 1.437-.719.382-.381.674-.718.944-.943"></path>
</svg>
      </a>

      <div class="d-flex flex-1 flex-order-2 text-right d-lg-none gap-2 flex-justify-end">
          <a
            href="/login?return_to=https%3A%2F%2Fgithub.com%2Fhumanlayer%2Fadvanced-context-engineering-for-coding-agents%2Fblob%2Fmain%2Fwsff.md"
            class="HeaderMenu-link HeaderMenu-button d-inline-flex f5 no-underline border color-border-default rounded-2 px-2 py-1 color-fg-inherit js-prevent-focus-on-mobile-nav"
            data-hydro-click="{&quot;event_type&quot;:&quot;authentication.click&quot;,&quot;payload&quot;:{&quot;location_in_page&quot;:&quot;site header menu&quot;,&quot;repository_id&quot;:null,&quot;auth_type&quot;:&quot;SIGN_UP&quot;,&quot;originating_url&quot;:&quot;https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/wsff.md&quot;,&quot;user_id&quot;:null}}" data-hydro-click-hmac="7eff8582fc59af0b6e2df88c478e44d452243dfe88f917934113585995b9b603"
            data-analytics-event="{&quot;category&quot;:&quot;Marketing nav&quot;,&quot;action&quot;:&quot;click to Sign in&quot;,&quot;label&quot;:&quot;ref_page:Marketing;ref_cta:Sign in;ref_loc:Header&quot;}"
          >
            Sign in
          </a>
              <div class="AppHeader-appearanceSettings">
    <react-partial-anchor>        <button data-target="react-partial-anchor.anchor" id="icon-button-aee1ef81-cd71-4121-aa1e-1554815b8e63" aria-labelledby="tooltip-48673591-b9d4-4e18-bedf-39982118b21f" type="button" disabled="disabled" data-view-component="true" class="Button Button--iconOnly Button--invisible Button--medium AppHeader-button HeaderMenu-link border cursor-wait">  <svg aria-hidden="true" data-component="Octicon" height="16" viewBox="0 0 16 16" version="1.1" width="16" data-view-component="true" class="octicon octicon-sliders Button-visual">
    <path d="M15 2.75a.75.75 0 0 1-.75.75h-4a.75.75 0 0 1 0-1.5h4a.75.75 0 0 1 .75.75Zm-8.5.75v1.25a.75.75 0 0 0 1.5 0v-4a.75.75 0 0 0-1.5 0V2H1.75a.75.75 0 0 0 0 1.5H6.5Zm1.25 5.25a.75.75 0 0 0 0-1.5h-6a.75.75 0 0 0 0 1.5h6ZM15 8a.75.75 0 0 1-.75.75H11.5V10a.75.75 0 1 1-1.5 0V6a.75.75 0 0 1 1.5 0v1.25h2.75A.75.75 0 0 1 15 8Zm-9 5.25v-2a.75.75 0 0 0-1.5 0v1.25H1.75a.75.75 0 0 0 0 1.5H4.5v1.25a.75.75 0 0 0 1.5 0v-2Zm9 0a.75.75 0 0 1-.75.75h-6a.75.75 0 0 1 0-1.5h6a.75.75 0 0 1 .75.75Z"></path>
</svg>
</button><tool-tip id="tooltip-48673591-b9d4-4e18-bedf-39982118b21f" for="icon-button-aee1ef81-cd71-4121-aa1e-1554815b8e63" popover="manual" data-direction="s" data-type="label" data-view-component="true" class="sr-only position-absolute">Appearance settings</tool-tip>

<template data-target="react-partial-anchor.template"><link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/primer-react-css.ba5192c6c34cad29.module.css" />
<link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/appearance-settings.50e7ffeded21c6c0.module.css" />

<react-partial
  partial-name="appearance-settings"
  data-ssr="false"
  data-attempted-ssr="false"
  data-react-profiling="false"
>
  
  <script type="application/json" data-target="react-partial.embeddedData">{"props":{}}</script>
  <div data-target="react-partial.reactRoot"></div>
</react-partial>

</template></react-partial-anchor>  </div>

      </div>
    </div>


    <div class="HeaderMenu js-header-menu height-fit position-lg-relative d-lg-flex flex-column flex-auto top-0">
      <div class="HeaderMenu-wrapper d-flex flex-column flex-self-start flex-lg-row flex-auto rounded rounded-lg-0">
          <link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/71236-18053476e03a7169.js" fetchpriority="low" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/64670-754a2dd94b7cfb79.js" fetchpriority="low" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/20522-7084c3d40a461eaa.js" fetchpriority="low" />
<link crossorigin="anonymous" rel="modulepreload" href="https://github.githubassets.com/assets/marketing-navigation-aac7fd44be3fe745.js" fetchpriority="low" />
<link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/primer-react-css.ba5192c6c34cad29.module.css" />
<link crossorigin="anonymous" media="all" rel="stylesheet" href="https://github.githubassets.com/assets/marketing-navigation.60c4aa8a2e5fca55.module.css" />

<react-partial
  partial-name="marketing-navigation"
  data-ssr="true"
  data-attempted-ssr="true"
  data-react-profiling="false"
>
  
  <script type="application/json" data-target="react-partial.embeddedData">{"props":{"should_use_dotcom_links":true}}</script>
  <div data-target="react-partial.reactRoot"><nav class="MarketingNavigation-module__nav__W0KYY" aria-label="Global"><ul class="MarketingNavigation-module__list__tFbMb"><li><div class="NavDropdown-module__container__l2YeI"><button type="button" class="NavDropdown-module__button__PEHWX" aria-expanded="false" aria-controls="_R_5_">Platform<svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-chevron-right NavDropdown-module__buttonIcon__Tkl8_" viewBox="0 0 16 16" width="16" height="16" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M6.22 3.22a.75.75 0 0 1 1.06 0l4.25 4.25a.75.75 0 0 1 0 1.06l-4.25 4.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042L9.94 8 6.22 4.28a.75.75 0 0 1 0-1.06Z"></path></svg></button><div id="_R_5_" class="NavDropdown-module__dropdown__xm1jd"><ul class="NavDropdown-module__list__zuCgG"><li><div class="NavGroup-module__group__W8SqJ"><span class="NavGroup-module__title__Wzxz2" id="_R_1d5_">AI CODE CREATION</span><ul class="NavGroup-module__list__UCOFy" aria-labelledby="_R_1d5_"><li><a href="https://github.com/features/copilot" data-analytics-event="{&quot;action&quot;:&quot;github_copilot&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;github_copilot_link_platform_navbar&quot;}" class="NavLink-module__link__EG3d4"><div class="NavLink-module__text__XvpLQ"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-copilot NavLink-module__icon__ltGNM" viewBox="0 0 24 24" width="24" height="24" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M23.922 16.992c-.861 1.495-5.859 5.023-11.922 5.023-6.063 0-11.061-3.528-11.922-5.023A.641.641 0 0 1 0 16.736v-2.869a.841.841 0 0 1 .053-.22c.372-.935 1.347-2.292 2.605-2.656.167-.429.414-1.055.644-1.517a10.195 10.195 0 0 1-.052-1.086c0-1.331.282-2.499 1.132-3.368.397-.406.89-.717 1.474-.952 1.399-1.136 3.392-2.093 6.122-2.093 2.731 0 4.767.957 6.166 2.093.584.235 1.077.546 1.474.952.85.869 1.132 2.037 1.132 3.368 0 .368-.014.733-.052 1.086.23.462.477 1.088.644 1.517 1.258.364 2.233 1.721 2.605 2.656a.832.832 0 0 1 .053.22v2.869a.641.641 0 0 1-.078.256ZM12.172 11h-.344a4.323 4.323 0 0 1-.355.508C10.703 12.455 9.555 13 7.965 13c-1.725 0-2.989-.359-3.782-1.259a2.005 2.005 0 0 1-.085-.104L4 11.741v6.585c1.435.779 4.514 2.179 8 2.179 3.486 0 6.565-1.4 8-2.179v-6.585l-.098-.104s-.033.045-.085.104c-.793.9-2.057 1.259-3.782 1.259-1.59 0-2.738-.545-3.508-1.492a4.323 4.323 0 0 1-.355-.508h-.016.016Zm.641-2.935c.136 1.057.403 1.913.878 2.497.442.544 1.134.938 2.344.938 1.573 0 2.292-.337 2.657-.751.384-.435.558-1.15.558-2.361 0-1.14-.243-1.847-.705-2.319-.477-.488-1.319-.862-2.824-1.025-1.487-.161-2.192.138-2.533.529-.269.307-.437.808-.438 1.578v.021c0 .265.021.562.063.893Zm-1.626 0c.042-.331.063-.628.063-.894v-.02c-.001-.77-.169-1.271-.438-1.578-.341-.391-1.046-.69-2.533-.529-1.505.163-2.347.537-2.824 1.025-.462.472-.705 1.179-.705 2.319 0 1.211.175 1.926.558 2.361.365.414 1.084.751 2.657.751 1.21 0 1.902-.394 2.344-.938.475-.584.742-1.44.878-2.497Z"></path><path d="M14.5 14.25a1 1 0 0 1 1 1v2a1 1 0 0 1-2 0v-2a1 1 0 0 1 1-1Zm-5 0a1 1 0 0 1 1 1v2a1 1 0 0 1-2 0v-2a1 1 0 0 1 1-1Z"></path></svg><span class="NavLink-module__title__Q7t0p">GitHub Copilot</span><span class="NavLink-module__subtitle__X4gkW">Write better code with AI</span></div></a></li><li><a href="https://github.com/features/ai/github-app" data-analytics-event="{&quot;action&quot;:&quot;github_copilot_app&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;github_copilot_app_link_platform_navbar&quot;}" class="NavLink-module__link__EG3d4"><div class="NavLink-module__text__XvpLQ"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-mark-github NavLink-module__icon__ltGNM" viewBox="0 0 24 24" width="24" height="24" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M10.226 17.284c-2.965-.36-5.054-2.493-5.054-5.256 0-1.123.404-2.336 1.078-3.144-.292-.741-.247-2.314.09-2.965.898-.112 2.111.36 2.83 1.01.853-.269 1.752-.404 2.853-.404 1.1 0 1.999.135 2.807.382.696-.629 1.932-1.1 2.83-.988.315.606.36 2.179.067 2.942.72.854 1.101 2 1.101 3.167 0 2.763-2.089 4.852-5.098 5.234.763.494 1.28 1.572 1.28 2.807v2.336c0 .674.561 1.056 1.235.786 4.066-1.55 7.255-5.615 7.255-10.646C23.5 6.188 18.334 1 11.978 1 5.62 1 .5 6.188.5 12.545c0 4.986 3.167 9.12 7.435 10.669.606.225 1.19-.18 1.19-.786V20.63a2.9 2.9 0 0 1-1.078.224c-1.483 0-2.359-.808-2.987-2.313-.247-.607-.517-.966-1.034-1.033-.27-.023-.359-.135-.359-.27 0-.27.45-.471.898-.471.652 0 1.213.404 1.797 1.235.45.651.921.943 1.483.943.561 0 .92-.202 1.437-.719.382-.381.674-.718.944-.943"></path></svg><span class="NavLink-module__title__Q7t0p">GitHub Copilot app</span><span class="NavLink-module__subtitle__X4gkW">Direct agents from issue to merge</span></div></a></li><li><a href="https://github.com/mcp" data-analytics-event="{&quot;action&quot;:&quot;mcp_registry&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;mcp_registry_link_platform_navbar&quot;}" class="NavLink-module__link__EG3d4"><div class="NavLink-module__text__XvpLQ"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-mcp NavLink-module__icon__ltGNM" viewBox="0 0 24 24" width="24" height="24" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M9.795 1.694a4.287 4.287 0 0 1 6.061 0 4.28 4.28 0 0 1 1.181 3.819 4.282 4.282 0 0 1 3.819 1.181 4.287 4.287 0 0 1 0 6.061l-6.793 6.793a.249.249 0 0 0 0 .353l2.617 2.618a.75.75 0 1 1-1.061 1.061l-2.617-2.618a1.75 1.75 0 0 1 0-2.475l6.793-6.793a2.785 2.785 0 1 0-3.939-3.939l-5.9 5.9a.734.734 0 0 1-.249.165.749.749 0 0 1-.812-1.225l5.9-5.901a2.785 2.785 0 1 0-3.939-3.939L2.931 10.68A.75.75 0 1 1 1.87 9.619l7.925-7.925Z"></path><path d="M12.42 4.069a.752.752 0 0 1 1.061 0 .752.752 0 0 1 0 1.061L7.33 11.28a2.788 2.788 0 0 0 0 3.94 2.788 2.788 0 0 0 3.94 0l6.15-6.151a.752.752 0 0 1 1.061 0 .752.752 0 0 1 0 1.061l-6.151 6.15a4.285 4.285 0 1 1-6.06-6.06l6.15-6.151Z"></path></svg><span class="NavLink-module__title__Q7t0p">MCP Registry<sup class="NavLink-module__label__bil7n">New</sup></span><span class="NavLink-module__subtitle__X4gkW">Integrate external tools</span></div></a></li></ul></div></li><li><div class="NavGroup-module__group__W8SqJ"><span class="NavGroup-module__title__Wzxz2" id="_R_2d5_">DEVELOPER WORKFLOWS</span><ul class="NavGroup-module__list__UCOFy" aria-labelledby="_R_2d5_"><li><a href="https://github.com/features/actions" data-analytics-event="{&quot;action&quot;:&quot;actions&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;actions_link_platform_navbar&quot;}" class="NavLink-module__link__EG3d4"><div class="NavLink-module__text__XvpLQ"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-workflow NavLink-module__icon__ltGNM" viewBox="0 0 24 24" width="24" height="24" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M1 3a2 2 0 0 1 2-2h6.5a2 2 0 0 1 2 2v6.5a2 2 0 0 1-2 2H7v4.063C7 16.355 7.644 17 8.438 17H12.5v-2.5a2 2 0 0 1 2-2H21a2 2 0 0 1 2 2V21a2 2 0 0 1-2 2h-6.5a2 2 0 0 1-2-2v-2.5H8.437A2.939 2.939 0 0 1 5.5 15.562V11.5H3a2 2 0 0 1-2-2Zm2-.5a.5.5 0 0 0-.5.5v6.5a.5.5 0 0 0 .5.5h6.5a.5.5 0 0 0 .5-.5V3a.5.5 0 0 0-.5-.5ZM14.5 14a.5.5 0 0 0-.5.5V21a.5.5 0 0 0 .5.5H21a.5.5 0 0 0 .5-.5v-6.5a.5.5 0 0 0-.5-.5Z"></path></svg><span class="NavLink-module__title__Q7t0p">Actions</span><span class="NavLink-module__subtitle__X4gkW">Automate any workflow</span></div></a></li><li><a href="https://github.com/features/codespaces" data-analytics-event="{&quot;action&quot;:&quot;codespaces&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;codespaces_link_platform_navbar&quot;}" class="NavLink-module__link__EG3d4"><div class="NavLink-module__text__XvpLQ"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon-codespaces NavLink-module__icon__ltGNM" viewBox="0 0 24 24" width="24" height="24" fill="currentColor" display="inline-block" overflow="visible" style="vertical-align:text-bottom"><path d="M3.5 3.75C3.5 2.784 4.284 2 5.25 2h13.5c.966 0 1.75.784 1.75 1.75v7.5A1.75 1.75 0 0 1 18.75 13H5.25a1.75 1.75 0 0 1-1.75-1.75Zm-2 12c0-.966.784-1.75 1.75-1.75h17.5c.966 0 1.75.784 1.75 1.75v4a1.75 1.75 0 0 1-1.75 1.75H3.25a1.75 1.75 0 0 1-1.75-1.75ZM5.25 3.5a.25.25 0 0 0-.25.25v7.5c0 .138.112.25.25.25h13.5a.25.25 0 0 0 .25-.25v-7.5a.25.25 0 0 0-.25-.25Zm-2 12a.25.25 0 0 0-.25.25v4c0 .138.112.25.25.25h17.5a.25.25 0 0 0 .25-.25v-4a.25.25 0 0 0-.25-.25Z"></path><path d="M10 17.75a.75.75 0 0 1 .75-.75h6.5a.75.75 0 0 1 0 1.5h-6.5a.75.75 0 0 1-.75-.75Zm-4 0a.75.75 0 0 1 .75-.75h.5a.75.75 0 0 1 0 1.5h-.5a.75.75 0 0 1-.75-.75Z"></path></svg><span class="NavLink-module__title__Q7t0p">Codespaces</span><span class="NavLink-module__subtitle__X4gkW">Instant dev environments</span></div></a></li><li><a href="https://github.com/features/issues" data-analytics-event="{&quot;action&quot;:&quot;issues&quot;,&quot;tag&quot;:&quot;link&quot;,&quot;context&quot;:&quot;platform&quot;,&quot;location&quot;:&quot;navbar&quot;,&quot;label&quot;:&quot;issues_link_platform_navbar&quot;}" class="NavLink-module__link__EG3d4"><div class="NavLink-module__text__XvpLQ"><svg data-component="Octicon" aria-hidden="true" focusable="false" class="octicon octicon