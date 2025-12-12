# JSON Prompt Examples

Ready-to-use JSON schemas for common use cases.

## Marketing Images

### Beverage Can - Premium Seltzer

```json
{
  "marketing_image": {
    "meta": {
      "spec_version": "1.0.0",
      "title": "Aurora Lime Hero Shot",
      "campaign": "aurora_lime_launch_q3",
      "brand_name": "Aurora Lime",
      "usage_context": "web"
    },
    "subject": {
      "type": "product_can",
      "name": "Aurora Lime Seltzer",
      "variant": "Original Lime",
      "physical_properties": {
        "volume_oz": 12,
        "dimensions": "standard 12oz beverage can",
        "finish": "matte"
      }
    },
    "props": {
      "foreground": [
        {"type": "lime_slice", "count": 3, "position": "front_left", "notes": "fresh lime slices, visible pulp and rind"}
      ],
      "midground": [
        {"type": "ice_cube", "count": 12, "position": "around_base", "notes": "partially melted, small reflections"}
      ],
      "background": []
    },
    "environment": {
      "surface": {
        "material": "glossy",
        "reflection_strength": 0.7
      },
      "background": {
        "color": "#003b47",
        "texture": "smooth",
        "effect": "bokeh_soft"
      },
      "atmosphere": {
        "mood": "refreshing, premium, night-time bar feel",
        "keywords": ["sparkling", "cool", "luminous", "evening"]
      }
    },
    "camera": {
      "angle": "three_quarter_front",
      "framing": "medium_close",
      "focal_length_mm": 50,
      "depth_of_field": "medium"
    },
    "lighting": {
      "key_light_direction": "right",
      "key_light_intensity": "high",
      "fill_light_direction": "left",
      "fill_light_intensity": "low",
      "rim_light": false,
      "color_temperature": "neutral"
    },
    "brand": {
      "logo_asset": "aurora_lime_logo.png",
      "primary_colors": ["#00ffc2", "#003b47"],
      "must_match_assets": ["aurora_lime_logo.png"],
      "forbidden_changes": ["do_not_change_logo", "do_not_change_brand_name"]
    },
    "controls": {
      "lock_subject_geometry": true,
      "lock_logo_and_label": true,
      "allow_background_variation": false,
      "allow_prop_relayout": "small_only"
    }
  }
}
```

**Rendered prompt:**
> 12oz Aurora Lime Seltzer can, matte finish, three-quarter front angle, medium-close framing. Fresh lime slices (3) in front left, ice cubes (12) around base. Glossy reflective surface, dark teal background (#003b47) with soft bokeh effect. Key light from right at high intensity, fill from left at low intensity, neutral color temperature. Premium beverage photography, refreshing mood, 4K resolution.

---

### Skincare Product - Luxury Serum

```json
{
  "marketing_image": {
    "meta": {
      "spec_version": "1.0.0",
      "title": "Radiance Serum Hero",
      "campaign": "spring_skincare_2025",
      "brand_name": "Lumière",
      "usage_context": "social"
    },
    "subject": {
      "type": "cosmetic",
      "name": "Radiance Vitamin C Serum",
      "variant": "30ml dropper bottle",
      "physical_properties": {
        "volume_oz": 1,
        "dimensions": "30ml amber glass dropper bottle",
        "finish": "glossy"
      }
    },
    "props": {
      "foreground": [
        {"type": "water_droplet", "count": 15, "position": "on_subject", "notes": "condensation on glass"},
        {"type": "citrus_slice", "count": 2, "position": "front_right", "notes": "orange slices for vitamin C theme"}
      ],
      "midground": [
        {"type": "leaf", "count": 3, "position": "around_base", "notes": "eucalyptus leaves"}
      ],
      "background": []
    },
    "environment": {
      "surface": {
        "material": "marble",
        "reflection_strength": 0.4
      },
      "background": {
        "color": "#FFF5E6",
        "texture": null,
        "effect": "gradient"
      },
      "atmosphere": {
        "mood": "luxury, spa, wellness",
        "keywords": ["clean", "premium", "natural", "radiant"]
      }
    },
    "camera": {
      "angle": "front",
      "framing": "close_up",
      "focal_length_mm": 85,
      "depth_of_field": "shallow"
    },
    "lighting": {
      "key_light_direction": "top_left",
      "key_light_intensity": "medium",
      "fill_light_direction": "right",
      "fill_light_intensity": "low",
      "rim_light": true,
      "color_temperature": "warm"
    },
    "brand": {
      "logo_asset": null,
      "primary_colors": ["#FFD700", "#FFFFFF", "#2C1810"],
      "must_match_assets": [],
      "forbidden_changes": ["do_not_change_bottle_shape"]
    },
    "controls": {
      "lock_subject_geometry": true,
      "lock_logo_and_label": true,
      "allow_background_variation": true,
      "allow_prop_relayout": "small_only"
    }
  }
}
```

---

### Tech Product - Wireless Earbuds

```json
{
  "marketing_image": {
    "meta": {
      "spec_version": "1.0.0",
      "title": "SoundPods Pro Launch",
      "campaign": "soundpods_launch",
      "brand_name": "SoundPods",
      "usage_context": "web"
    },
    "subject": {
      "type": "device",
      "name": "SoundPods Pro",
      "variant": "Midnight Black",
      "physical_properties": {
        "volume_oz": null,
        "dimensions": "wireless earbuds with charging case",
        "finish": "matte"
      }
    },
    "props": {
      "foreground": [],
      "midground": [
        {"type": "particle_effect", "count": 1, "position": "around_subject", "notes": "subtle floating particles/dust motes"}
      ],
      "background": []
    },
    "environment": {
      "surface": {
        "material": "none",
        "reflection_strength": 0
      },
      "background": {
        "color": "#0A0A0A",
        "texture": null,
        "effect": "gradient_radial"
      },
      "atmosphere": {
        "mood": "premium tech, sleek, modern",
        "keywords": ["minimal", "futuristic", "elegant"]
      }
    },
    "camera": {
      "angle": "three_quarter_front",
      "framing": "medium",
      "focal_length_mm": 50,
      "depth_of_field": "deep"
    },
    "lighting": {
      "key_light_direction": "top",
      "key_light_intensity": "high",
      "fill_light_direction": "front",
      "fill_light_intensity": "medium",
      "rim_light": true,
      "color_temperature": "cool"
    },
    "brand": {
      "logo_asset": null,
      "primary_colors": ["#000000", "#FFFFFF"],
      "must_match_assets": [],
      "forbidden_changes": []
    },
    "controls": {
      "lock_subject_geometry": true,
      "lock_logo_and_label": true,
      "allow_background_variation": true,
      "allow_prop_relayout": "none"
    }
  }
}
```

---

## UI/UX Mockups

### SaaS Dashboard - Analytics

```json
{
  "ui_builder": {
    "meta": {
      "spec_version": "1.0.0",
      "name": "Acme Analytics Dashboard",
      "description": "Marketing analytics dashboard with KPIs and charts",
      "author": "Design Team",
      "tags": ["saas", "analytics", "dashboard"]
    },
    "app": {
      "platform": "web",
      "fidelity": "high-fi",
      "viewport": {
        "width": 1440,
        "height": 900
      },
      "theme": "light"
    },
    "tokens": {
      "color": {
        "primary": "#2563EB",
        "secondary": "#64748B",
        "background": "#F9FAFB",
        "surface": "#FFFFFF",
        "accent": "#10B981",
        "text_primary": "#111827",
        "text_secondary": "#6B7280"
      },
      "typography": {
        "font_family": "Inter",
        "headline_size": 24,
        "body_size": 14,
        "caption_size": 12
      },
      "radius": {
        "sm": 4,
        "md": 8,
        "lg": 12,
        "full": 9999
      },
      "spacing_scale": [0, 4, 8, 12, 16, 24, 32, 48]
    },
    "screens": [
      {
        "id": "dashboard_main",
        "name": "Dashboard Overview",
        "role": "primary",
        "layout": {
          "containers": [
            {"id": "top_nav", "type": "stack", "subtype": "horizontal", "region": "top_nav", "children": []},
            {"id": "sidebar", "type": "stack", "subtype": "vertical", "region": "sidebar", "children": []},
            {"id": "content", "type": "grid", "subtype": "auto", "region": "content", "children": []}
          ]
        }
      }
    ],
    "components": [
      {"id": "navbar", "screen_id": "dashboard_main", "container_id": "top_nav", "component_type": "navbar", "props": {"logo_text": "Acme Analytics", "avatar_initials": "NJ"}, "data_binding": null},
      {"id": "nav_list", "screen_id": "dashboard_main", "container_id": "sidebar", "component_type": "sidebar_nav", "props": {"items": ["Overview", "Channels", "Cohorts", "Settings"], "active": "Overview"}, "data_binding": null},
      {"id": "kpi_grid", "screen_id": "dashboard_main", "container_id": "content", "component_type": "kpi_grid", "props": {"cards": [{"label": "Sessions", "value": "124,983", "trend": "+12%"}, {"label": "Signups", "value": "3,942", "trend": "+8%"}, {"label": "Conversion", "value": "3.2%", "trend": "+0.4%"}]}, "data_binding": {"source": "analytics_api"}},
      {"id": "traffic_chart", "screen_id": "dashboard_main", "container_id": "content", "component_type": "line_chart", "props": {"title": "Daily Traffic (Last 30 Days)", "series": ["sessions", "signups"]}, "data_binding": {"source": "analytics_api"}},
      {"id": "campaigns_table", "screen_id": "dashboard_main", "container_id": "content", "component_type": "data_table", "props": {"columns": ["Campaign", "Spend", "Clicks", "CPC"], "rows": 5}, "data_binding": {"source": "campaigns_api"}}
    ],
    "constraints": {
      "layout_lock": true,
      "theme_lock": false,
      "content_lock": false,
      "min_tap_target": 44
    }
  }
}
```

---

### Mobile App - Fitness Tracker

```json
{
  "ui_builder": {
    "meta": {
      "spec_version": "1.0.0",
      "name": "FitTrack Mobile App",
      "description": "Habit tracking app with dark mode",
      "author": "Mobile Team",
      "tags": ["mobile", "fitness", "habits", "dark_mode"]
    },
    "app": {
      "platform": "mobile",
      "fidelity": "high-fi",
      "viewport": {
        "width": 390,
        "height": 844
      },
      "theme": "dark"
    },
    "tokens": {
      "color": {
        "primary": "#8B5CF6",
        "secondary": "#64748B",
        "background": "#0F172A",
        "surface": "#1E293B",
        "accent": "#22D3EE",
        "text_primary": "#F8FAFC",
        "text_secondary": "#94A3B8"
      },
      "typography": {
        "font_family": "SF Pro Display",
        "headline_size": 28,
        "body_size": 16,
        "caption_size": 13
      },
      "radius": {
        "sm": 8,
        "md": 12,
        "lg": 16,
        "full": 9999
      },
      "spacing_scale": [0, 4, 8, 16, 24, 32]
    },
    "screens": [
      {
        "id": "home",
        "name": "Today's Habits",
        "role": "primary",
        "layout": {
          "containers": [
            {"id": "header", "type": "stack", "subtype": "horizontal", "region": "top_nav", "children": []},
            {"id": "main", "type": "stack", "subtype": "vertical", "region": "content", "children": []},
            {"id": "tab_bar", "type": "stack", "subtype": "horizontal", "region": "footer", "children": []}
          ]
        }
      },
      {
        "id": "calendar",
        "name": "Calendar View",
        "role": "secondary",
        "layout": {
          "containers": [
            {"id": "cal_header", "type": "stack", "subtype": "horizontal", "region": "top_nav", "children": []},
            {"id": "cal_grid", "type": "grid", "subtype": "7_columns", "region": "content", "children": []}
          ]
        }
      },
      {
        "id": "stats",
        "name": "Statistics",
        "role": "secondary",
        "layout": {
          "containers": [
            {"id": "stats_header", "type": "stack", "subtype": "horizontal", "region": "top_nav", "children": []},
            {"id": "stats_content", "type": "stack", "subtype": "vertical", "region": "content", "children": []}
          ]
        }
      }
    ],
    "components": [
      {"id": "greeting", "screen_id": "home", "container_id": "header", "component_type": "text", "props": {"text": "Good morning!", "style": "headline"}, "data_binding": null},
      {"id": "habit_list", "screen_id": "home", "container_id": "main", "component_type": "list", "props": {"items": [{"name": "Meditate", "streak": 12, "completed": true}, {"name": "Exercise", "streak": 5, "completed": false}, {"name": "Read", "streak": 8, "completed": false}]}, "data_binding": {"source": "habits_db"}},
      {"id": "progress_ring", "screen_id": "home", "container_id": "main", "component_type": "progress_ring", "props": {"value": 0.66, "label": "2 of 3 complete"}, "data_binding": null},
      {"id": "tab_nav", "screen_id": "home", "container_id": "tab_bar", "component_type": "tab_bar", "props": {"tabs": ["Home", "Calendar", "Stats", "Settings"], "active": "Home"}, "data_binding": null}
    ],
    "constraints": {
      "layout_lock": true,
      "theme_lock": true,
      "content_lock": false,
      "min_tap_target": 44
    }
  }
}
```

---

### Creative UI - Alien Control Panel

```json
{
  "ui_builder": {
    "meta": {
      "spec_version": "1.0.0",
      "name": "Xeno Command Interface",
      "description": "Fictional alien spacecraft control panel",
      "author": "Concept Artist",
      "tags": ["sci-fi", "concept", "alien", "creative"]
    },
    "app": {
      "platform": "desktop",
      "fidelity": "high-fi",
      "viewport": {
        "width": 1920,
        "height": 1080
      },
      "theme": "custom"
    },
    "tokens": {
      "color": {
        "primary": "#19FFB3",
        "secondary": "#FF1493",
        "background": "#050016",
        "surface": "#0D0628",
        "accent": "#00BFFF",
        "text_primary": "#E0FFFF",
        "text_secondary": "#7B68EE"
      },
      "typography": {
        "font_family": "Orbitron",
        "headline_size": 32,
        "body_size": 14,
        "caption_size": 11
      },
      "radius": {
        "sm": 0,
        "md": 2,
        "lg": 4,
        "full": 9999
      },
      "spacing_scale": [0, 4, 8, 16, 24, 48]
    },
    "screens": [
      {
        "id": "command_bridge",
        "name": "Command Bridge",
        "role": "primary",
        "layout": {
          "containers": [
            {"id": "left_panel", "type": "stack", "subtype": "vertical", "region": "sidebar", "children": []},
            {"id": "center_display", "type": "grid", "subtype": "auto", "region": "content", "children": []},
            {"id": "right_panel", "type": "stack", "subtype": "vertical", "region": "sidebar", "children": []},
            {"id": "status_bar", "type": "stack", "subtype": "horizontal", "region": "footer", "children": []}
          ]
        }
      },
      {
        "id": "star_map",
        "name": "Stellar Navigation",
        "role": "secondary",
        "layout": {
          "containers": [
            {"id": "map_display", "type": "flex", "subtype": "full", "region": "content", "children": []}
          ]
        }
      }
    ],
    "components": [
      {"id": "nav_controls", "screen_id": "command_bridge", "container_id": "left_panel", "component_type": "gauge_cluster", "props": {"gauges": ["velocity", "altitude", "fuel", "shields"]}, "data_binding": null},
      {"id": "main_viewport", "screen_id": "command_bridge", "container_id": "center_display", "component_type": "viewport", "props": {"type": "hologram", "content": "space_view"}, "data_binding": null},
      {"id": "btn_first_contact", "screen_id": "command_bridge", "container_id": "center_display", "component_type": "button", "props": {"label": "INITIATE FIRST CONTACT", "variant": "primary_glow", "icon": "antenna"}, "data_binding": null},
      {"id": "comms_panel", "screen_id": "command_bridge", "container_id": "right_panel", "component_type": "comms_display", "props": {"channels": ["Alpha", "Beta", "Gamma"], "active": "Alpha"}, "data_binding": null},
      {"id": "system_status", "screen_id": "command_bridge", "container_id": "status_bar", "component_type": "status_strip", "props": {"items": ["LIFE SUPPORT: NOMINAL", "REACTOR: 98%", "COMMS: ACTIVE"]}, "data_binding": null}
    ],
    "constraints": {
      "layout_lock": true,
      "theme_lock": true,
      "content_lock": false,
      "min_tap_target": 44
    },
    "_comment": "Creative concept piece - alien aesthetic with neon colors and sci-fi typography"
  }
}
```

---

## Diagrams & Infographics

### Software Development Flowchart

```json
{
  "diagram_spec": {
    "meta": {
      "spec_version": "1.0.0",
      "title": "CI/CD Pipeline Flow",
      "description": "Software deployment pipeline from commit to production",
      "author": "DevOps Team",
      "tags": ["devops", "cicd", "pipeline", "flowchart"]
    },
    "canvas": {
      "width": 1920,
      "height": 600,
      "unit": "px",
      "direction": "left_to_right",
      "grid": {
        "columns": 12,
        "margin": 48
      }
    },
    "semantics": {
      "diagram_type": "flowchart",
      "primary_relationship": "control_flow",
      "swimlanes": []
    },
    "tokens": {
      "color": {
        "primary": "#3B82F6",
        "secondary": "#64748B",
        "success": "#10B981",
        "warning": "#F59E0B",
        "error": "#EF4444",
        "background": "#FFFFFF",
        "border": "#E5E7EB"
      },
      "typography": {
        "font_family": "Inter",
        "node_label_size": 14,
        "edge_label_size": 11,
        "section_title_size": 18
      }
    },
    "sections": [
      {"id": "main", "name": "Pipeline", "height_percent": 100, "layout_type": "full_width"}
    ],
    "nodes": [
      {"id": "commit", "label": "Git Commit", "role": "start", "section_id": "main", "position": {"x": 100, "y": 250}, "size": {"width": 120, "height": 60}, "style": {"shape": "rounded", "fill_color": "#DBEAFE", "border_color": "#3B82F6"}},
      {"id": "build", "label": "Build", "role": "process", "section_id": "main", "position": {"x": 280, "y": 250}, "size": {"width": 120, "height": 60}, "style": {"shape": "rectangle", "fill_color": "#FEF3C7", "border_color": "#F59E0B"}},
      {"id": "test", "label": "Run Tests", "role": "process", "section_id": "main", "position": {"x": 460, "y": 250}, "size": {"width": 120, "height": 60}, "style": {"shape": "rectangle", "fill_color": "#FEF3C7", "border_color": "#F59E0B"}},
      {"id": "decision", "label": "Tests Pass?", "role": "decision", "section_id": "main", "position": {"x": 640, "y": 250}, "size": {"width": 100, "height": 100}, "style": {"shape": "diamond", "fill_color": "#F3E8FF", "border_color": "#8B5CF6"}},
      {"id": "staging", "label": "Deploy Staging", "role": "process", "section_id": "main", "position": {"x": 820, "y": 200}, "size": {"width": 140, "height": 60}, "style": {"shape": "rectangle", "fill_color": "#DCFCE7", "border_color": "#10B981"}},
      {"id": "prod", "label": "Deploy Production", "role": "end", "section_id": "main", "position": {"x": 1020, "y": 200}, "size": {"width": 160, "height": 60}, "style": {"shape": "rounded", "fill_color": "#10B981", "border_color": "#059669"}},
      {"id": "fix", "label": "Fix Issues", "role": "process", "section_id": "main", "position": {"x": 640, "y": 400}, "size": {"width": 120, "height": 60}, "style": {"shape": "rectangle", "fill_color": "#FEE2E2", "border_color": "#EF4444"}}
    ],
    "edges": [
      {"id": "e1", "from": "commit", "to": "build", "label": "", "style": {"line_type": "straight", "arrowhead": "standard"}},
      {"id": "e2", "from": "build", "to": "test", "label": "", "style": {"line_type": "straight", "arrowhead": "standard"}},
      {"id": "e3", "from": "test", "to": "decision", "label": "", "style": {"line_type": "straight", "arrowhead": "standard"}},
      {"id": "e4", "from": "decision", "to": "staging", "label": "Yes", "style": {"line_type": "orthogonal", "arrowhead": "standard"}},
      {"id": "e5", "from": "staging", "to": "prod", "label": "", "style": {"line_type": "straight", "arrowhead": "standard"}},
      {"id": "e6", "from": "decision", "to": "fix", "label": "No", "style": {"line_type": "orthogonal", "arrowhead": "standard"}},
      {"id": "e7", "from": "fix", "to": "commit", "label": "", "style": {"line_type": "curved", "arrowhead": "standard"}}
    ],
    "groups": [],
    "data_constraints": [],
    "legend": {
      "show": true,
      "items": [
        {"label": "Start/End", "shape": "rounded", "fill_color": "#DBEAFE"},
        {"label": "Process", "shape": "rectangle", "fill_color": "#FEF3C7"},
        {"label": "Decision", "shape": "diamond", "fill_color": "#F3E8FF"}
      ]
    },
    "constraints": {
      "layout_lock": false,
      "allow_auto_routing": true,
      "preserve_data_accuracy": true
    },
    "production": {
      "resolution_dpi": 150,
      "export_formats": ["png", "svg"],
      "min_contrast_ratio": 4.5
    }
  }
}
```

---

### Sports Statistics Infographic

```json
{
  "diagram_spec": {
    "meta": {
      "spec_version": "1.0.0",
      "title": "Carolina Basketball - 20 Years of Excellence",
      "description": "Statistics poster for basketball program anniversary",
      "author": "Sports Graphics",
      "tags": ["sports", "infographic", "statistics", "basketball"]
    },
    "canvas": {
      "width": 1800,
      "height": 2700,
      "unit": "px",
      "direction": "top_to_bottom",
      "grid": {
        "columns": 12,
        "margin": 48
      }
    },
    "semantics": {
      "diagram_type": "infographic",
      "primary_relationship": "hierarchy",
      "swimlanes": []
    },
    "tokens": {
      "color": {
        "primary": "#7BAFD4",
        "secondary": "#13294B",
        "accent": "#C4A052",
        "background": "#FFFFFF",
        "border": "#E5E7EB",
        "text_dark": "#13294B",
        "text_light": "#FFFFFF"
      },
      "typography": {
        "font_family": "Bebas Neue",
        "node_label_size": 48,
        "edge_label_size": 14,
        "section_title_size": 72
      }
    },
    "sections": [
      {"id": "header", "name": "Header", "height_percent": 12, "layout_type": "full_width"},
      {"id": "big_numbers", "name": "Key Statistics", "height_percent": 15, "layout_type": "five_column"},
      {"id": "timeline", "name": "Championship Timeline", "height_percent": 18, "layout_type": "full_width"},
      {"id": "leaders", "name": "All-Time Leaders", "height_percent": 25, "layout_type": "two_column"},
      {"id": "records", "name": "Program Records", "height_percent": 20, "layout_type": "three_column"},
      {"id": "footer", "name": "Footer", "height_percent": 10, "layout_type": "full_width"}
    ],
    "nodes": [
      {"id": "title", "label": "20 YEARS OF EXCELLENCE", "role": "header", "section_id": "header", "position": {"x": 900, "y": 100}, "size": {"width": 1600, "height": 200}, "style": {"shape": "rectangle", "fill_color": "#13294B", "border_color": "#13294B"}, "data": {}},
      {"id": "stat_wins", "label": "567", "role": "data", "section_id": "big_numbers", "position": {"x": 180, "y": 400}, "size": {"width": 300, "height": 150}, "style": {"shape": "rectangle", "fill_color": "#7BAFD4", "border_color": "#7BAFD4"}, "data": {"sublabel": "WINS", "value": 567}},
      {"id": "stat_losses", "label": "197", "role": "data", "section_id": "big_numbers", "position": {"x": 540, "y": 400}, "size": {"width": 300, "height": 150}, "style": {"shape": "rectangle", "fill_color": "#FFFFFF", "border_color": "#13294B"}, "data": {"sublabel": "LOSSES", "value": 197}},
      {"id": "stat_pct", "label": "74.2%", "role": "data", "section_id": "big_numbers", "position": {"x": 900, "y": 400}, "size": {"width": 300, "height": 150}, "style": {"shape": "rectangle", "fill_color": "#C4A052", "border_color": "#C4A052"}, "data": {"sublabel": "WIN PCT", "value": "74.2%"}},
      {"id": "stat_titles", "label": "4", "role": "data", "section_id": "big_numbers", "position": {"x": 1260, "y": 400}, "size": {"width": 300, "height": 150}, "style": {"shape": "rectangle", "fill_color": "#13294B", "border_color": "#13294B"}, "data": {"sublabel": "CONF TITLES", "value": 4}},
      {"id": "stat_ncaa", "label": "18", "role": "data", "section_id": "big_numbers", "position": {"x": 1620, "y": 400}, "size": {"width": 300, "height": 150}, "style": {"shape": "rectangle", "fill_color": "#7BAFD4", "border_color": "#7BAFD4"}, "data": {"sublabel": "NCAA APPEARANCES", "value": 18}}
    ],
    "edges": [],
    "groups": [],
    "data_constraints": [
      {"field": "Overall Record", "value": "567-197", "must_match": true},
      {"field": "Win Percentage", "value": "74.2%", "must_match": true},
      {"field": "Conference Titles", "value": "4", "must_match": true},
      {"field": "NCAA Tournament Appearances", "value": "18", "must_match": true},
      {"field": "Total Points (All-Time)", "value": "61,808", "must_match": true}
    ],
    "legend": {
      "show": false,
      "items": []
    },
    "constraints": {
      "layout_lock": true,
      "allow_auto_routing": false,
      "preserve_data_accuracy": true
    },
    "production": {
      "resolution_dpi": 300,
      "export_formats": ["png", "pdf"],
      "min_contrast_ratio": 4.5
    },
    "_comment": "Sports statistics poster - data_constraints list values that MUST appear exactly as specified for verification"
  }
}
```

---

## Quick Reference: Iteration Patterns

### Lighting A/B Test

**Version A:**
```json
"lighting": {
  "key_light_direction": "right",
  "key_light_intensity": "high",
  "color_temperature": "neutral"
}
```

**Version B:**
```json
"lighting": {
  "key_light_direction": "left",
  "key_light_intensity": "medium",
  "color_temperature": "warm"
}
```

### Camera Angle Variations

```json
// Hero shot
"camera": {"angle": "three_quarter_front", "framing": "medium"}

// Detail shot
"camera": {"angle": "front", "framing": "close_up"}

// Context shot
"camera": {"angle": "overhead", "framing": "wide"}
```

### Theme Swap (Same Structure)

**Light theme:**
```json
"tokens": {
  "color": {
    "background": "#FFFFFF",
    "surface": "#F9FAFB",
    "text_primary": "#111827"
  }
}
```

**Dark theme:**
```json
"tokens": {
  "color": {
    "background": "#0F172A",
    "surface": "#1E293B",
    "text_primary": "#F8FAFC"
  }
}
```
