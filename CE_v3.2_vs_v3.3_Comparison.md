# Cyber Essentials v3.2 vs v3.3 Comparison

**Document comparison analysis**

## Available Documents

| Document Type                           | v3.2 (April 2025)       | v3.3 (April 2026)       |
|-----------------------------------------|-------------------------|-------------------------|
| **Requirements for IT Infrastructure**  | ✅ Available            | ✅ Available            |
| **Test Specification (CE Plus)**        | ✅ Available            | ❌ Not available (TBD)  |

---

## Executive Summary

### What Changed from v3.2 to v3.3 (Requirements)

**Major Changes:**
1. **Cloud Services Mandatory** — Explicit statement added: "Cloud services cannot be excluded from scope"
2. **New Cloud Service Definition** — Formal definition added to Definitions section
3. **Expanded Passwordless Authentication** — Updated to explicitly include FIDO2/Passkeys
4. **Backup Guidance Elevated** — Moved from Further Guidance to new dedicated section (Section C)
5. **Software Development References** — Now references "Software Security Code of Practice" instead of OWASP ASVS
6. **Scope Language Updated** — Removed "untrusted connections" terminology

**Minor Changes:**
- Section reorganization (Backup moved from E to C)
- Clarified definitions (Software, Vulnerability fixes, Passwordless authentication)
- Updated MFA definition to include "Multi-Factor Authentication (MFA)" abbreviation
- Enhanced Zero Trust guidance wording

---

## Section-by-Section Detailed Comparison

### 1. What's New (Change Log)

#### v3.2 "What's new in this version" (lines 59-73)
```
• Passwordless guidance added to User Access Control
• Software definition updated
• Vulnerability fix definition added
• Passwordless definition and description added
• Update to security update management control to include
  vulnerabilities that are fixed by manual configuration only
• References to 'home working' changed to 'home and remote working'
```

#### v3.3 "What's new in this version" (lines 17-20)
```
• Definition for 'cloud services' provided
• Updated definition for Passwordless Authentication to include FIDO2
• Definitive statement that cloud services cannot be excluded from scope
• Software Security Code of Practice introduced in Software Development section
• Scope criteria no longer refers to 'untrusted connections'
• Importance of backing up data is emphasised
```

**Analysis:** Each version documents changes from the *previous* version, so these lists don't overlap.

---

### 2. Definitions Section

#### NEW in v3.3: Cloud Service Definition (v3.3:36)
```
Cloud service means an on-demand, scalable service, hosted on shared infrastructure,
and accessible via the internet. For the purposes of Cyber Essentials, a cloud service
will be accessed via an account (which may be credentials issued by your organisation,
or an email address used for business purposes), and will store or process data for
your organisation
```
**Impact:** HIGH — Provides clear criteria for what constitutes a cloud service in scope.

#### NEW in v3.3: Multi-Factor Authentication (MFA) definition (v3.3:40)
```
Multi-Factor Authentication (MFA) is a method of authenticating a user which uses
two or more verification factors
```
**Impact:** LOW — Simple abbreviation clarification, was implicit in v3.2.

#### UPDATED: Passwordless Authentication Definition

**v3.2 (lines 162-164):**
```
Passwordless authentication is an authentication method that uses a factor other than
user knowledge to establish identity. Examples include but are not limited to; biometric
data, physical devices, one-time codes, QR codes, and push notifications.
```

**v3.3 (lines 47):**
```
Passwordless authentication is a method to establish a user's identity that uses a factor
other than knowledge. Examples include but are not limited to: FIDO2 authenticators,
biometric data, security keys or tokens, one-time codes, QR codes, and push notifications.
```

**Key Change:** **FIDO2 authenticators** explicitly added to the definition.

**Impact:** MEDIUM — Aligns with industry standards (FIDO2/WebAuthn), clarifies acceptable passwordless methods.

---

### 3. NEW Section C: Backing up your data

#### v3.2 Location
"Backing up your data" was in **Section E: Further guidance** (lines 999-1011), *after* Zero Trust guidance.

#### v3.3 Location
"Backing up your data" is now **Section C** (lines 48-55), positioned *before* Scope section.

**v3.3 Content (lines 48-55):**
```
Backing up your data is not a technical requirement of Cyber Essentials. However, we
highly recommend implementing an appropriate backup solution. Backing up means creating
a copy of your information and saving it to another device or to cloud storage (online).

Backing up regularly means you will always have a recent version of your information saved.
This will help you recover quicker if your data is lost or stolen.

If automatic backups are available, you should consider turning them on. This will regularly
save your information into cloud storage, without you having to remember.

If you back up your information to a USB stick or an external hard drive, disconnect it from
your computer when a backup isn't being done.
```

**Impact:** HIGH — Elevation to Section C signals increased importance, though still "not a technical requirement."

**Rationale:** Likely response to ransomware incidents where organizations with CE certification still suffered data loss.

---

### 4. Scope Section

#### REMOVED: "Untrusted Connections" Language

**v3.2 (lines 185-191):**
```
The requirements apply to all devices and software in scope and which meet any of
these conditions:
• can accept incoming network connections from untrusted internet-connected hosts
• can establish user-initiated outbound connections to devices via the internet
• control the flow of data between any of the above devices and the internet
```

**v3.3 (lines 62-65):**
```
The requirements apply to all devices and software in scope and which meet any of
these conditions:
• can accept incoming network connections from internet-connected devices
• can establish outbound connections to devices via the internet
• control the flow of data between any of the above devices and the internet
```

**Key Changes:**
1. "untrusted internet-connected hosts" → "internet-connected devices"
2. "user-initiated outbound" → "outbound" (removed "user-initiated")

**Impact:** MEDIUM — Simplifies language, removes ambiguous "untrusted" term (aligns with Zero Trust principles where all connections are treated as untrusted by default).

#### NEW in v3.3: Cloud Services Mandatory Statement (v3.3:69)

**v3.2 (line 280):**
```
If your organisation's data or services are hosted on cloud services, these services must
be in scope.
```

**v3.3 (lines 68-69):**
```
A scope that doesn't include end-user devices isn't acceptable. If your organisation's data
or services are hosted on cloud services, these services must be in scope. Cloud services
cannot be excluded from scope.
```

**Key Addition:** **"Cloud services cannot be excluded from scope."** — Emphatic clarification.

**Impact:** HIGH — Eliminates any ambiguity about excluding cloud services from certification scope.

---

### 5. Software Development / Web Applications Section

#### UPDATED: Reference to Best Practices

**v3.2 (lines 497-509) — Section "vii. Web applications":**
```
Publicly available commercial web applications (rather than apps developed in-house) are
in scope by default. Bespoke and custom components of web applications are out of scope.
The best way to mitigate vulnerabilities in applications is robust development and testing
in line with commercial best practice, such as the OWASP Application Security Verification
Standard | OWASP Foundation.
```

**v3.3 (lines 181-182) — Section "(vii) Software development":**
```
Publicly available commercial web applications (rather than apps developed in-house) are
in scope by default. Bespoke and custom components of web applications are out of scope.
The best way to mitigate vulnerabilities in applications is robust development and testing
in line with commercial best practice. See the Software Security Code of Practice for
further details.
```

**Key Changes:**
1. Section title: "Web applications" → "Software development"
2. Reference changed: "OWASP Application Security Verification Standard | OWASP Foundation" → "Software Security Code of Practice"

**Impact:** MEDIUM — Shifts from specific OWASP standard to broader UK government guidance (likely referring to NCSC's Secure Development and Deployment Guidance or similar).

---

### 6. User Access Control — Passwordless Authentication

#### UPDATED: Expanded Guidance and FIDO2 Details

**v3.2 (lines 902-926) — Section "Passwordless authentication":**
```
Passwordless authentication is a method of verifying identity without using traditional passwords.

Common examples of passwordless authentication include:
• Biometric authentication: Uses biological traits of the user such as fingerprints or
  facial features to confirm their identity.
• Security keys or tokens: Physical hardware devices such as USB security keys or smart cards.
• One-time codes: Temporary codes are sent via email, SMS, or a mobile app.
• Push notifications: A prompt on a smartphone to approve or deny a login attempt.

This helps to avoid many of the problems with traditional passwords which can be forgotten,
stolen, or brute-forced.
```

**v3.3 (lines 301-309) — Section "Passwordless authentication":**
```
Passwordless authentication is a method of verifying identity without using traditional passwords.

Common examples of passwordless authentication include:
• Passkeys: Passwordless login technology based on public-key cryptography used to securely
  authenticate a user. This includes FIDO2 authenticators which are considered as Passkeys.
  FIDO2 authenticators are regarded as MFA because user authentication is performed. FIDO2
  is a set of standards that define cryptographic authentication using public key credentials
  and protocols to provide more secure alternatives to passwords for accessing online services
• Biometric authentication: Uses biological traits of the user such as fingerprints or facial
  features to confirm their identity
• Security keys or tokens: Physical hardware devices such as USB security keys or smart cards
• Push notifications: A prompt on a smartphone to approve or deny a login attempt
• One-time codes: Temporary codes are sent via email, SMS, or a mobile app

This helps to avoid many of the problems with traditional passwords which can be forgotten,
stolen, or brute-forced.
```

**Key Additions:**
1. **Passkeys** section added with detailed FIDO2 explanation
2. **"FIDO2 authenticators are regarded as MFA"** — Important clarification
3. Reordered list (Passkeys first, one-time codes moved to end)

**Impact:** HIGH — Aligns with modern authentication standards (Apple Passkeys, Google Passkeys, Microsoft Windows Hello). Clarifies that FIDO2 = MFA by default.

---

### 7. Zero Trust Guidance

#### UPDATED: Minor Wording Changes

**v3.2 (lines 1031-1036):**
```
A zero trust architecture is an approach to system design where inherent trust in the
network is removed. Instead, the network is assumed hostile and each access request is
verified, based on an access policy. Confidence in a request is achieved by building context,
which relies on strong authentication, authorisation, device health, and value of the data
being accessed.
```

**v3.3 (lines 364):**
```
A zero trust architecture is an approach to system design where inherent trust in the
network is removed. Instead the network is assumed to be hostile, and each access request
is verified based on an access policy. Confidence in a request is achieved by building
context, which relies on strong authentication, authorisation, device health, and value of
the data being accessed.
```

**Key Changes:**
- "assumed hostile and each" → "assumed to be hostile, and each"
- "verified, based on" → "verified based on"

**Impact:** NEGLIGIBLE — Stylistic/grammatical improvements only.

---

## Summary Table: Requirements v3.2 vs v3.3

| Section                      | v3.2                                         | v3.3                                              | Impact |
|------------------------------|----------------------------------------------|---------------------------------------------------|--------|
| **Cloud Service Definition** | Not defined                                  | **NEW:** Formal definition added                  | HIGH   |
| **Cloud Mandatory**          | "must be in scope"                           | "**cannot be excluded from scope**"               | HIGH   |
| **Backup Section**           | Section E (Further Guidance)                 | **Section C** (elevated)                          | HIGH   |
| **Passwordless Auth**        | Basic definition                             | **FIDO2/Passkeys** added, MFA equivalence noted   | HIGH   |
| **Scope Language**           | "untrusted connections"                      | Removed "untrusted"                               | MEDIUM |
| **Software Dev**             | References OWASP ASVS                        | References "Software Security Code of Practice"   | MEDIUM |
| **MFA Definition**           | Implicit                                     | Explicit abbreviation added                       | LOW    |
| **Zero Trust**               | Section E                                    | Section F (no content change)                     | LOW    |

---

## Test Specification Status

**Test Spec v3.2** (April 2025) is the latest available. **Test Spec v3.3** does not yet exist.

This is expected — test specifications typically lag behind requirements updates to allow time for:
1. Certification Bodies to update testing procedures
2. Tool vendors to align vulnerability scanners
3. Assessor training on new requirements

**Prediction:** Test Spec v3.3 will likely be released in late 2026 or early 2027, incorporating:
- Updated cloud service testing procedures (scope verification)
- FIDO2/Passkey authentication testing
- Backup solution verification (advisory, not mandatory)

---

## Actionable Recommendations

### For Organizations Currently Implementing CE v3.2
1. **Immediate:** Prepare to include all cloud services in scope (no exceptions)
2. **Q4 2026:** Deploy FIDO2/Passkeys where feasible (Microsoft/Google/Apple support)
3. **Ongoing:** Implement backup solutions (not required, but "highly recommend" → likely future requirement)
4. **Review:** Ensure software development practices align with NCSC guidance, not just OWASP

### For Organizations Planning CE Certification
1. **Use v3.3 Requirements** (April 2026) as the baseline
2. **Test against v3.2 Test Spec** (April 2025) until v3.3 Test Spec released
3. **Proactively implement:**
   - Cloud service inventory and scope documentation
   - FIDO2/Passkey rollout plan
   - Backup solution (3-2-1 rule: 3 copies, 2 media types, 1 offsite)

---

## Document Metadata

- **Analysis Date:** 2026-09-09
- **Comparison Tool:** pdftotext + diff
- **Source Files:**
  - `cyber-essentials-requirements-for-it-infrastructure-v3-2.pdf` (April 2025)
  - `cyber-essentials-requirements-for-it-infrastructure-v3-3.pdf` (April 2026)
  - `cyber-essentials-plus-test-specification-v3-2.pdf` (April 2025)

---

## Appendix: Line-by-Line Diff Summary

Total diff lines: **1,342 lines** (including context)

**Key structural changes:**
1. Section C added (Backup) — ~8 lines
2. Definitions expanded — ~40 lines
3. Passwordless authentication section expanded — ~15 lines
4. Scope language updated — ~10 lines
5. Software development references updated — ~5 lines
6. Page numbering/formatting changes — ~1,200 lines (cosmetic)

**Net substantive changes:** ~80 lines of meaningful content updates.

---

*End of Comparison Document*
