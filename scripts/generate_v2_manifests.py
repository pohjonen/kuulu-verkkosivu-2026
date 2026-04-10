#!/usr/bin/env python3
"""
Generate machine-readable Kuulu v2 manifests from curated planning data.

Outputs:
- docs/generated/kuulu-v2-page-manifest.json
- docs/generated/kuulu-v2-module-manifest.json

These manifests are intended to be consumed by future automation,
HubSpot implementation helpers, and validation scripts.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path("/workspace")
GENERATED = ROOT / "docs" / "generated"


PAGE_MANIFEST = [
    {
        "slug": "/v2-etusivu",
        "id": "homepage-v2",
        "url": "https://www.kuulu.fi/",
        "source_url": "https://www.kuulu.fi/",
        "page_type": "homepage",
        "template": "homepage-v2",
        "section_stack": [
            "hero-cinematic-v2",
            "problem-grid-v2",
            "audience-split-v2",
            "service-pillars-v2",
            "process-steps-v2",
            "stats-trust-band-v2",
            "reference-grid-v2",
            "final-cta-v2",
        ],
        "content_sources": ["live", "notion:Etusivu", "notion:Kuulu etusivu draft", "pdf:Zero Click"],
        "criticality": "highest",
    },
    {
        "slug": "/v2-videotuotanto",
        "id": "video-service-v2",
        "url": "https://www.kuulu.fi/videotuotanto",
        "source_url": "https://www.kuulu.fi/videotuotanto",
        "page_type": "video-service",
        "template": "video-service-landing-v2",
        "section_stack": [
            "hero-cinematic-v2",
            "problem-grid-v2",
            "video-model-comparison-v2",
            "service-pillars-v2",
            "process-steps-v2",
            "stats-trust-band-v2",
            "reference-grid-v2",
            "faq-v2",
            "final-cta-v2",
        ],
        "content_sources": ["live", "notion:Kuulu Videotuotanto — Sivuteksti v1", "pdf:Zero Click"],
        "criticality": "high",
    },
    {
        "slug": "/v2-koulutus",
        "id": "training-v2",
        "url": "https://www.kuulu.fi/koulutus",
        "source_url": "https://www.kuulu.fi/koulutus",
        "page_type": "training",
        "template": "training-landing-v2",
        "section_stack": [
            "hero-cinematic-v2",
            "problem-grid-v2",
            "service-pillars-v2",
            "process-steps-v2",
            "training-agenda-v2",
            "stats-trust-band-v2",
            "faq-v2",
            "final-cta-v2",
        ],
        "content_sources": ["live", "notion:Koulutus", "pdf:Zero Click"],
        "criticality": "high",
    },
    {
        "slug": "/v2-digimarkkinointi",
        "id": "digimarkkinointi-v2",
        "url": "https://www.kuulu.fi/digimarkkinointi",
        "source_url": "https://www.kuulu.fi/digimarkkinointi",
        "page_type": "service",
        "template": "service-landing-v2",
        "section_stack": [
            "hero-cinematic-v2",
            "problem-grid-v2",
            "audience-split-v2",
            "service-pillars-v2",
            "process-steps-v2",
            "reference-grid-v2",
            "faq-v2",
            "final-cta-v2",
        ],
        "content_sources": ["live", "pdf:Zero Click"],
        "criticality": "high",
    },
    {
        "slug": "/v2-case-studies",
        "id": "case-studies-v2",
        "url": "https://www.kuulu.fi/case-studies",
        "source_url": "https://www.kuulu.fi/case-studies",
        "page_type": "reference-index",
        "template": "reference-index-v2",
        "section_stack": [
            "hero-cinematic-v2",
            "reference-grid-v2",
            "reference-grid-v2",
            "final-cta-v2",
        ],
        "content_sources": ["live", "brand"],
        "criticality": "medium",
    },
    {
        "slug": "/v2-yhteystiedot",
        "id": "yhteystiedot-v2",
        "url": "https://www.kuulu.fi/yhteystiedot",
        "source_url": "https://www.kuulu.fi/yhteystiedot",
        "page_type": "company-info",
        "template": "company-info-v2",
        "section_stack": [
            "hero-cinematic-v2",
            "lead-capture-form-cta-v2",
            "team-grid-v2",
            "contact-info-v2",
            "final-cta-v2",
        ],
        "content_sources": ["live", "brand"],
        "criticality": "medium",
        "must_not_touch_live_dependencies": True,
    },
]


MODULE_MANIFEST = [
    {
        "module": "hero-cinematic-v2",
        "module_key": "hero-cinematic-v2",
        "used_on": [
            "homepage-v2",
            "service-landing-v2",
            "training-landing-v2",
            "video-service-landing-v2",
            "reference-detail-v2",
            "company-info-v2",
        ],
        "required_field_groups": ["content", "cta", "media", "layout", "style", "advanced"],
        "build_wave": 1,
        "depends_on": ["theme-tokens-v2", "cta-patterns-v2", "media-wrapper-v2"],
        "field_groups": ["content", "cta", "media", "layout", "style", "advanced"],
        "guardrails": {
            "max_ctas": 2,
            "max_media_slots": 1,
            "supports_free_rich_text": False,
        },
    },
    {
        "module": "final-cta-v2",
        "module_key": "final-cta-v2",
        "used_on": [
            "homepage-v2",
            "service-landing-v2",
            "training-landing-v2",
            "video-service-landing-v2",
            "reference-index-v2",
            "reference-detail-v2",
            "company-info-v2",
        ],
        "required_field_groups": ["content", "cta", "layout", "style", "advanced"],
        "build_wave": 1,
        "depends_on": ["cta-patterns-v2", "spacing-tokens-v2"],
        "field_groups": ["content", "cta", "layout", "style", "advanced"],
        "guardrails": {
            "max_ctas": 2,
            "supports_free_rich_text": False,
        },
    },
    {
        "module_key": "lead-capture-form-cta-v2",
        "module": "lead-capture-form-cta-v2",
        "used_on": ["company-info-v2"],
        "required_field_groups": ["content", "cta", "media", "layout", "style", "advanced"],
        "build_wave": 2,
        "depends_on": ["cta-patterns-v2", "form-selector-v2", "safe-link-field-v2"],
        "field_groups": ["content", "cta", "media", "layout", "style", "advanced"],
        "guardrails": {
            "requires_primary_cta_or_form": True,
            "supported_media_modes": ["none", "image", "icon"],
            "supports_free_rich_text": False,
        },
    },
    {
        "module": "problem-grid-v2",
        "module_key": "problem-grid-v2",
        "used_on": [
            "homepage-v2",
            "service-landing-v2",
            "training-landing-v2",
            "video-service-landing-v2",
        ],
        "required_field_groups": ["content", "layout", "style", "advanced"],
        "build_wave": 1,
        "depends_on": ["icon-system-v2", "card-surface-v2"],
        "field_groups": ["content", "layout", "style", "advanced"],
        "guardrails": {
            "card_min": 3,
            "card_max": 6,
            "supports_free_rich_text": False,
        },
    },
    {
        "module": "service-pillars-v2",
        "module_key": "service-pillars-v2",
        "used_on": [
            "homepage-v2",
            "service-landing-v2",
            "training-landing-v2",
            "video-service-landing-v2",
        ],
        "required_field_groups": ["content", "cta", "media", "layout", "style", "advanced"],
        "build_wave": 1,
        "depends_on": ["card-grid-v2", "micro-cta-v2"],
        "field_groups": ["content", "cta", "media", "layout", "style", "advanced"],
        "guardrails": {
            "card_max": 4,
            "supports_free_rich_text": False,
        },
    },
    {
        "module": "audience-split-v2",
        "module_key": "audience-split-v2",
        "used_on": ["homepage-v2", "service-landing-v2", "training-landing-v2"],
        "required_field_groups": ["content", "cta", "layout", "style", "advanced"],
        "build_wave": 2,
        "depends_on": ["grid-two-column-v2", "stats-labels-v2"],
        "field_groups": ["content", "cta", "layout", "style", "advanced"],
        "guardrails": {
            "fixed_blocks": 2,
            "default_percentages": ["95", "5"],
        },
    },
    {
        "module": "process-steps-v2",
        "module_key": "process-steps-v2",
        "used_on": [
            "homepage-v2",
            "service-landing-v2",
            "training-landing-v2",
            "video-service-landing-v2",
        ],
        "required_field_groups": ["content", "layout", "style", "advanced"],
        "build_wave": 2,
        "depends_on": ["repeater-step-logic-v2", "heading-hierarchy-v2"],
        "field_groups": ["content", "layout", "style", "advanced"],
        "guardrails": {
            "step_min": 3,
            "step_max": 6,
            "auto_numbering": True,
        },
    },
    {
        "module": "stats-trust-band-v2",
        "module_key": "stats-trust-band-v2",
        "used_on": [
            "homepage-v2",
            "training-landing-v2",
            "video-service-landing-v2",
            "reference-detail-v2",
        ],
        "required_field_groups": ["content", "layout", "style", "advanced"],
        "build_wave": 2,
        "depends_on": ["typography-tokens-v2", "spacing-tokens-v2"],
        "field_groups": ["content", "layout", "style", "advanced"],
        "guardrails": {
            "stat_min": 2,
            "stat_max": 5,
        },
    },
    {
        "module": "reference-grid-v2",
        "module_key": "reference-grid-v2",
        "used_on": [
            "homepage-v2",
            "service-landing-v2",
            "video-service-landing-v2",
            "reference-index-v2",
        ],
        "required_field_groups": ["content", "cta", "media", "layout", "style", "advanced"],
        "build_wave": 2,
        "depends_on": ["image-card-v2", "safe-link-field-v2"],
        "field_groups": ["content", "cta", "media", "layout", "style", "advanced"],
        "guardrails": {
            "supports_free_rich_text": False,
            "link_types": ["internal_page", "validated_url"],
        },
    },
    {
        "module": "video-model-comparison-v2",
        "module_key": "video-model-comparison-v2",
        "used_on": ["video-service-landing-v2"],
        "required_field_groups": ["content", "media", "layout", "style", "advanced"],
        "build_wave": 3,
        "depends_on": ["card-grid-v2", "media-wrapper-v2"],
        "field_groups": ["content", "media", "layout", "style", "advanced"],
        "guardrails": {
            "fixed_cards": 3,
            "locked_order": ["captured", "hybrid", "ai-enhanced"],
        },
    },
    {
        "module": "training-agenda-v2",
        "module_key": "training-agenda-v2",
        "used_on": ["training-landing-v2"],
        "required_field_groups": ["content", "layout", "style", "advanced"],
        "build_wave": 3,
        "depends_on": ["grouped-repeater-v2", "heading-hierarchy-v2"],
        "field_groups": ["content", "layout", "style", "advanced"],
        "guardrails": {
            "allowed_item_types": ["day", "core", "track", "module"],
            "supports_free_rich_text": False,
        },
    },
    {
        "module": "faq-v2",
        "module_key": "faq-v2",
        "used_on": ["training-landing-v2", "service-landing-v2", "video-service-landing-v2"],
        "required_field_groups": ["content", "layout", "style", "advanced"],
        "build_wave": 3,
        "depends_on": ["accordion-v2"],
        "field_groups": ["content", "layout", "style", "advanced"],
        "guardrails": {
            "faq_recommended_max": 8,
        },
    },
    {
        "module": "team-grid-v2",
        "module_key": "team-grid-v2",
        "used_on": ["company-info-v2", "person-profile-v2"],
        "required_field_groups": ["content", "media", "layout", "style", "advanced"],
        "build_wave": 3,
        "depends_on": ["people-card-v2", "image-ratio-v2"],
        "field_groups": ["content", "media", "layout", "style", "advanced"],
        "guardrails": {
            "supports_free_rich_text": False,
        },
    },
    {
        "module": "contact-info-v2",
        "module_key": "contact-info-v2",
        "used_on": ["company-info-v2"],
        "required_field_groups": ["content", "cta", "layout", "style", "advanced"],
        "build_wave": 3,
        "depends_on": ["structured-office-fields-v2", "safe-link-field-v2"],
        "field_groups": ["content", "cta", "layout", "style", "advanced"],
        "guardrails": {
            "rich_text_scope": "billing-only",
        },
    },
    {
        "module": "reference-detail-sections-v2",
        "module_key": "reference-detail-sections-v2",
        "used_on": ["reference-detail-v2"],
        "required_field_groups": ["content", "media", "layout", "style", "advanced"],
        "build_wave": 4,
        "depends_on": ["hero-cinematic-v2", "stats-trust-band-v2", "final-cta-v2"],
        "field_groups": ["content", "media", "layout", "style", "advanced"],
        "guardrails": {
            "enforced_order": [
                "case-hero",
                "key-facts",
                "challenge",
                "solution",
                "execution",
                "results",
                "testimonial",
                "cta",
            ]
        },
    },
]


def write_json(path: Path, payload):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    print(f"Wrote {path}")


def main():
    for page in PAGE_MANIFEST:
        page.setdefault("must_not_touch_live_dependencies", True)
    write_json(GENERATED / "kuulu-v2-page-manifest.json", PAGE_MANIFEST)
    write_json(GENERATED / "kuulu-v2-module-manifest.json", MODULE_MANIFEST)


if __name__ == "__main__":
    main()
