// This constant is provided because M_PI is nonstandard.
// This comes from Go's math.Pi, which in turn comes from http://oeis.org/A000796.

// TODO uiBool?

typedef struct uiInitOptions uiInitOptions;

struct uiInitOptions {
	size_t Size;
};

 const char *uiInit(uiInitOptions *options);
 void uiUninit(void);
 void uiFreeInitError(const char *err);

 void uiMain(void);
 void uiMainSteps(void);
 int uiMainStep(int wait);
 void uiQuit(void);

 void uiQueueMain(void (*f)(void *data), void *data);

 void uiOnShouldQuit(int (*f)(void *data), void *data);

 void uiFreeText(char *text);

typedef struct uiControl uiControl;

struct uiControl {
	uint32_t Signature;
	uint32_t OSSignature;
	uint32_t TypeSignature;
	void (*Destroy)(uiControl *);
	uintptr_t (*Handle)(uiControl *);
	uiControl *(*Parent)(uiControl *);
	void (*SetParent)(uiControl *, uiControl *);
	int (*Toplevel)(uiControl *);
	int (*Visible)(uiControl *);
	void (*Show)(uiControl *);
	void (*Hide)(uiControl *);
	int (*Enabled)(uiControl *);
	void (*Enable)(uiControl *);
	void (*Disable)(uiControl *);
};
// TOOD add argument names to all arguments

// TEST DOTDOTDOT
#define uiControl ...
 void uiControlDestroy(uiControl *);
 uintptr_t uiControlHandle(uiControl *);
 uiControl *uiControlParent(uiControl *);
 void uiControlSetParent(uiControl *, uiControl *);
 int uiControlToplevel(uiControl *);
 int uiControlVisible(uiControl *);
 void uiControlShow(uiControl *);
 void uiControlHide(uiControl *);
 int uiControlEnabled(uiControl *);
 void uiControlEnable(uiControl *);
 void uiControlDisable(uiControl *);

 uiControl *uiAllocControl(size_t n, uint32_t OSsig, uint32_t typesig, const char *typenamestr);
 void uiFreeControl(uiControl *);

// TODO make sure all controls have these
 void uiControlVerifySetParent(uiControl *, uiControl *);
 int uiControlEnabledToUser(uiControl *);

 void uiUserBugCannotSetParentOnToplevel(const char *type);

typedef struct uiWindow uiWindow;

// TEST DOTDOTDOT
#define uiWindow ...
 char *uiWindowTitle(uiWindow *w);
 void uiWindowSetTitle(uiWindow *w, const char *title);
 void uiWindowContentSize(uiWindow *w, int *width, int *height);
 void uiWindowSetContentSize(uiWindow *w, int width, int height);
 int uiWindowFullscreen(uiWindow *w);
 void uiWindowSetFullscreen(uiWindow *w, int fullscreen);
 void uiWindowOnContentSizeChanged(uiWindow *w, void (*f)(uiWindow *, void *), void *data);
 void uiWindowOnClosing(uiWindow *w, int (*f)(uiWindow *w, void *data), void *data);
 int uiWindowBorderless(uiWindow *w);
 void uiWindowSetBorderless(uiWindow *w, int borderless);
 void uiWindowSetChild(uiWindow *w, uiControl *child);
 int uiWindowMargined(uiWindow *w);
 void uiWindowSetMargined(uiWindow *w, int margined);
 uiWindow *uiNewWindow(const char *title, int width, int height, int hasMenubar);

typedef struct uiButton uiButton;
// TEST DOTDOTDOT
#define uiButton ...
 char *uiButtonText(uiButton *b);
 void uiButtonSetText(uiButton *b, const char *text);
 void uiButtonOnClicked(uiButton *b, void (*f)(uiButton *b, void *data), void *data);
 uiButton *uiNewButton(const char *text);

// TEST DOTDOTDOT
typedef struct uiBox uiBox;
#define uiBox ...
 void uiBoxAppend(uiBox *b, uiControl *child, int stretchy);
 void uiBoxDelete(uiBox *b, int index);
 int uiBoxPadded(uiBox *b);
 void uiBoxSetPadded(uiBox *b, int padded);
 uiBox *uiNewHorizontalBox(void);
 uiBox *uiNewVerticalBox(void);

typedef struct uiCheckbox uiCheckbox;
// TEST DOTDOTDOT
#define uiCheckbox ...
 char *uiCheckboxText(uiCheckbox *c);
 void uiCheckboxSetText(uiCheckbox *c, const char *text);
 void uiCheckboxOnToggled(uiCheckbox *c, void (*f)(uiCheckbox *c, void *data), void *data);
 int uiCheckboxChecked(uiCheckbox *c);
 void uiCheckboxSetChecked(uiCheckbox *c, int checked);
 uiCheckbox *uiNewCheckbox(const char *text);

typedef struct uiEntry uiEntry;
// TEST DOTDOTDOT
#define uiEntry ...
 char *uiEntryText(uiEntry *e);
 void uiEntrySetText(uiEntry *e, const char *text);
 void uiEntryOnChanged(uiEntry *e, void (*f)(uiEntry *e, void *data), void *data);
 int uiEntryReadOnly(uiEntry *e);
 void uiEntrySetReadOnly(uiEntry *e, int readonly);
 uiEntry *uiNewEntry(void);
 uiEntry *uiNewPasswordEntry(void);
 uiEntry *uiNewSearchEntry(void);

typedef struct uiLabel uiLabel;
// TEST DOTDOTDOT
#define uiLabel ...
 char *uiLabelText(uiLabel *l);
 void uiLabelSetText(uiLabel *l, const char *text);
 uiLabel *uiNewLabel(const char *text);

typedef struct uiTab uiTab;
// TEST DOTDOTDOT
#define uiTab ...
 void uiTabAppend(uiTab *t, const char *name, uiControl *c);
 void uiTabInsertAt(uiTab *t, const char *name, int before, uiControl *c);
 void uiTabDelete(uiTab *t, int index);
 int uiTabNumPages(uiTab *t);
 int uiTabMargined(uiTab *t, int page);
 void uiTabSetMargined(uiTab *t, int page, int margined);
 uiTab *uiNewTab(void);

typedef struct uiGroup uiGroup;
// TEST DOTDOTDOT
#define uiGroup ...
 char *uiGroupTitle(uiGroup *g);
 void uiGroupSetTitle(uiGroup *g, const char *title);
 void uiGroupSetChild(uiGroup *g, uiControl *c);
 int uiGroupMargined(uiGroup *g);
 void uiGroupSetMargined(uiGroup *g, int margined);
 uiGroup *uiNewGroup(const char *title);

// spinbox/slider rules:
// setting value outside of range will automatically clamp
// initial value is minimum
// complaint if min >= max?

typedef struct uiSpinbox uiSpinbox;
// TEST DOTDOTDOT
#define uiSpinbox ...
 int uiSpinboxValue(uiSpinbox *s);
 void uiSpinboxSetValue(uiSpinbox *s, int value);
 void uiSpinboxOnChanged(uiSpinbox *s, void (*f)(uiSpinbox *s, void *data), void *data);
 uiSpinbox *uiNewSpinbox(int min, int max);

typedef struct uiSlider uiSlider;
// TEST DOTDOTDOT
#define uiSlider ...
 int uiSliderValue(uiSlider *s);
 void uiSliderSetValue(uiSlider *s, int value);
 void uiSliderOnChanged(uiSlider *s, void (*f)(uiSlider *s, void *data), void *data);
 uiSlider *uiNewSlider(int min, int max);

typedef struct uiProgressBar uiProgressBar;
// TEST DOTDOTDOT
#define uiProgressBar ...
 int uiProgressBarValue(uiProgressBar *p);
 void uiProgressBarSetValue(uiProgressBar *p, int n);
 uiProgressBar *uiNewProgressBar(void);

typedef struct uiSeparator uiSeparator;
// TEST DOTDOTDOT
#define uiSeparator ...
 uiSeparator *uiNewHorizontalSeparator(void);
 uiSeparator *uiNewVerticalSeparator(void);

typedef struct uiCombobox uiCombobox;
// TEST DOTDOTDOT
#define uiCombobox ...
 void uiComboboxAppend(uiCombobox *c, const char *text);
 int uiComboboxSelected(uiCombobox *c);
 void uiComboboxSetSelected(uiCombobox *c, int n);
 void uiComboboxOnSelected(uiCombobox *c, void (*f)(uiCombobox *c, void *data), void *data);
 uiCombobox *uiNewCombobox(void);

typedef struct uiEditableCombobox uiEditableCombobox;
// TEST DOTDOTDOT
#define uiEditableCombobox ...
 void uiEditableComboboxAppend(uiEditableCombobox *c, const char *text);
 char *uiEditableComboboxText(uiEditableCombobox *c);
 void uiEditableComboboxSetText(uiEditableCombobox *c, const char *text);
// TODO what do we call a function that sets the currently selected item and fills the text field with it? editable comboboxes have no consistent concept of selected item
 void uiEditableComboboxOnChanged(uiEditableCombobox *c, void (*f)(uiEditableCombobox *c, void *data), void *data);
 uiEditableCombobox *uiNewEditableCombobox(void);

typedef struct uiRadioButtons uiRadioButtons;
// TEST DOTDOTDOT
#define uiRadioButtons ...
 void uiRadioButtonsAppend(uiRadioButtons *r, const char *text);
 int uiRadioButtonsSelected(uiRadioButtons *r);
 void uiRadioButtonsSetSelected(uiRadioButtons *r, int n);
 void uiRadioButtonsOnSelected(uiRadioButtons *r, void (*f)(uiRadioButtons *, void *), void *data);
 uiRadioButtons *uiNewRadioButtons(void);

typedef struct uiDateTimePicker uiDateTimePicker;
// TEST DOTDOTDOT
#define uiDateTimePicker ...
 uiDateTimePicker *uiNewDateTimePicker(void);
 uiDateTimePicker *uiNewDatePicker(void);
 uiDateTimePicker *uiNewTimePicker(void);

// TODO provide a facility for entering tab stops?
typedef struct uiMultilineEntry uiMultilineEntry;
// TEST DOTDOTDOT
#define uiMultilineEntry ...
 char *uiMultilineEntryText(uiMultilineEntry *e);
 void uiMultilineEntrySetText(uiMultilineEntry *e, const char *text);
 void uiMultilineEntryAppend(uiMultilineEntry *e, const char *text);
 void uiMultilineEntryOnChanged(uiMultilineEntry *e, void (*f)(uiMultilineEntry *e, void *data), void *data);
 int uiMultilineEntryReadOnly(uiMultilineEntry *e);
 void uiMultilineEntrySetReadOnly(uiMultilineEntry *e, int readonly);
 uiMultilineEntry *uiNewMultilineEntry(void);
 uiMultilineEntry *uiNewNonWrappingMultilineEntry(void);

typedef struct uiMenuItem uiMenuItem;
// TEST DOTDOTDOT
#define uiMenuItem ...
 void uiMenuItemEnable(uiMenuItem *m);
 void uiMenuItemDisable(uiMenuItem *m);
 void uiMenuItemOnClicked(uiMenuItem *m, void (*f)(uiMenuItem *sender, uiWindow *window, void *data), void *data);
 int uiMenuItemChecked(uiMenuItem *m);
 void uiMenuItemSetChecked(uiMenuItem *m, int checked);

typedef struct uiMenu uiMenu;
// TEST DOTDOTDOT
#define uiMenu ...
 uiMenuItem *uiMenuAppendItem(uiMenu *m, const char *name);
 uiMenuItem *uiMenuAppendCheckItem(uiMenu *m, const char *name);
 uiMenuItem *uiMenuAppendQuitItem(uiMenu *m);
 uiMenuItem *uiMenuAppendPreferencesItem(uiMenu *m);
 uiMenuItem *uiMenuAppendAboutItem(uiMenu *m);
 void uiMenuAppendSeparator(uiMenu *m);
 uiMenu *uiNewMenu(const char *name);

 char *uiOpenFile(uiWindow *parent);
 char *uiSaveFile(uiWindow *parent);
 void uiMsgBox(uiWindow *parent, const char *title, const char *description);
 void uiMsgBoxError(uiWindow *parent, const char *title, const char *description);

typedef struct uiArea uiArea;
typedef struct uiAreaHandler uiAreaHandler;
typedef struct uiAreaDrawParams uiAreaDrawParams;
typedef struct uiAreaMouseEvent uiAreaMouseEvent;
typedef struct uiAreaKeyEvent uiAreaKeyEvent;

typedef struct uiDrawContext uiDrawContext;

struct uiAreaHandler {
	void (*Draw)(uiAreaHandler *, uiArea *, uiAreaDrawParams *);
	// TODO document that resizes cause a full redraw for non-scrolling areas; implementation-defined for scrolling areas
	void (*MouseEvent)(uiAreaHandler *, uiArea *, uiAreaMouseEvent *);
	// TODO document that on first show if the mouse is already in the uiArea then one gets sent with left=0
	// TODO what about when the area is hidden and then shown again?
	void (*MouseCrossed)(uiAreaHandler *, uiArea *, int left);
	void (*DragBroken)(uiAreaHandler *, uiArea *);
	int (*KeyEvent)(uiAreaHandler *, uiArea *, uiAreaKeyEvent *);
};

// TODO RTL layouts?
// TODO reconcile edge and corner naming
typedef unsigned int uiWindowResizeEdge; enum{
	uiWindowResizeEdgeLeft,
	uiWindowResizeEdgeTop,
	uiWindowResizeEdgeRight,
	uiWindowResizeEdgeBottom,
	uiWindowResizeEdgeTopLeft,
	uiWindowResizeEdgeTopRight,
	uiWindowResizeEdgeBottomLeft,
	uiWindowResizeEdgeBottomRight,
	// TODO have one for keyboard resizes?
	// TODO GDK doesn't seem to have any others, including for keyboards...
	// TODO way to bring up the system menu instead?
};
// TEST DOTDOTDOT
#define uiArea ...
// TODO give a better name
// TODO document the types of width and height
 void uiAreaSetSize(uiArea *a, int width, int height);
// TODO uiAreaQueueRedraw()
 void uiAreaQueueRedrawAll(uiArea *a);
 void uiAreaScrollTo(uiArea *a, double x, double y, double width, double height);
// TODO document these can only be called within Mouse() handlers
// TODO should these be allowed on scrolling areas?
// TODO decide which mouse events should be accepted; Down is the only one guaranteed to work right now
// TODO what happens to events after calling this up to and including the next mouse up?
// TODO release capture?
 void uiAreaBeginUserWindowMove(uiArea *a);
 void uiAreaBeginUserWindowResize(uiArea *a, uiWindowResizeEdge edge);
 uiArea *uiNewArea(uiAreaHandler *ah);
 uiArea *uiNewScrollingArea(uiAreaHandler *ah, int width, int height);

struct uiAreaDrawParams {
	uiDrawContext *Context;

	// TODO document that this is only defined for nonscrolling areas
	double AreaWidth;
	double AreaHeight;

	double ClipX;
	double ClipY;
	double ClipWidth;
	double ClipHeight;
};

typedef struct uiDrawPath uiDrawPath;
typedef struct uiDrawBrush uiDrawBrush;
typedef struct uiDrawStrokeParams uiDrawStrokeParams;
typedef struct uiDrawMatrix uiDrawMatrix;

typedef struct uiDrawBrushGradientStop uiDrawBrushGradientStop;




typedef unsigned int uiDrawBrushType; enum {
	uiDrawBrushTypeSolid,
	uiDrawBrushTypeLinearGradient,
	uiDrawBrushTypeRadialGradient,
	uiDrawBrushTypeImage,
};

typedef unsigned int uiDrawLineCap; enum {
	uiDrawLineCapFlat,
	uiDrawLineCapRound,
	uiDrawLineCapSquare,
};

typedef unsigned int uiDrawLineJoin; enum {
	uiDrawLineJoinMiter,
	uiDrawLineJoinRound,
	uiDrawLineJoinBevel,
};

// this is the default for botoh cairo and Direct2D (in the latter case, from the C++ helper functions)
// Core Graphics doesn't explicitly specify a default, but NSBezierPath allows you to choose one, and this is the initial value
// so we're good to use it too!

typedef unsigned int uiDrawFillMode; enum {
	uiDrawFillModeWinding,
	uiDrawFillModeAlternate,
};

struct uiDrawMatrix {
	double M11;
	double M12;
	double M21;
	double M22;
	double M31;
	double M32;
};

struct uiDrawBrush {
	uiDrawBrushType Type;

	// solid brushes
	double R;
	double G;
	double B;
	double A;

	// gradient brushes
	double X0;		// linear: start X, radial: start X
	double Y0;		// linear: start Y, radial: start Y
	double X1;		// linear: end X, radial: outer circle center X
	double Y1;		// linear: end Y, radial: outer circle center Y
	double OuterRadius;		// radial gradients only
	uiDrawBrushGradientStop *Stops;
	size_t NumStops;
	// TODO extend mode
	// cairo: none, repeat, reflect, pad; no individual control
	// Direct2D: repeat, reflect, pad; no individual control
	// Core Graphics: none, pad; before and after individually
	// TODO cairo documentation is inconsistent about pad

	// TODO images

	// TODO transforms
};

struct uiDrawBrushGradientStop {
	double Pos;
	double R;
	double G;
	double B;
	double A;
};

struct uiDrawStrokeParams {
	uiDrawLineCap Cap;
	uiDrawLineJoin Join;
	// TODO what if this is 0? on windows there will be a crash with dashing
	double Thickness;
	double MiterLimit;
	double *Dashes;
	// TOOD what if this is 1 on Direct2D?
	// TODO what if a dash is 0 on Cairo or Quartz?
	size_t NumDashes;
	double DashPhase;
};

 uiDrawPath *uiDrawNewPath(uiDrawFillMode fillMode);
 void uiDrawFreePath(uiDrawPath *p);

 void uiDrawPathNewFigure(uiDrawPath *p, double x, double y);
 void uiDrawPathNewFigureWithArc(uiDrawPath *p, double xCenter, double yCenter, double radius, double startAngle, double sweep, int negative);
 void uiDrawPathLineTo(uiDrawPath *p, double x, double y);
// notes: angles are both relative to 0 and go counterclockwise
// TODO is the initial line segment on cairo and OS X a proper join?
// TODO what if sweep < 0?
 void uiDrawPathArcTo(uiDrawPath *p, double xCenter, double yCenter, double radius, double startAngle, double sweep, int negative);
 void uiDrawPathBezierTo(uiDrawPath *p, double c1x, double c1y, double c2x, double c2y, double endX, double endY);
// TODO quadratic bezier
 void uiDrawPathCloseFigure(uiDrawPath *p);

// TODO effect of these when a figure is already started
 void uiDrawPathAddRectangle(uiDrawPath *p, double x, double y, double width, double height);

 void uiDrawPathEnd(uiDrawPath *p);

 void uiDrawStroke(uiDrawContext *c, uiDrawPath *path, uiDrawBrush *b, uiDrawStrokeParams *p);
 void uiDrawFill(uiDrawContext *c, uiDrawPath *path, uiDrawBrush *b);

// TODO primitives:
// - rounded rectangles
// - elliptical arcs
// - quadratic bezier curves

 void uiDrawMatrixSetIdentity(uiDrawMatrix *m);
 void uiDrawMatrixTranslate(uiDrawMatrix *m, double x, double y);
 void uiDrawMatrixScale(uiDrawMatrix *m, double xCenter, double yCenter, double x, double y);
 void uiDrawMatrixRotate(uiDrawMatrix *m, double x, double y, double amount);
 void uiDrawMatrixSkew(uiDrawMatrix *m, double x, double y, double xamount, double yamount);
 void uiDrawMatrixMultiply(uiDrawMatrix *dest, uiDrawMatrix *src);
 int uiDrawMatrixInvertible(uiDrawMatrix *m);
 int uiDrawMatrixInvert(uiDrawMatrix *m);
 void uiDrawMatrixTransformPoint(uiDrawMatrix *m, double *x, double *y);
 void uiDrawMatrixTransformSize(uiDrawMatrix *m, double *x, double *y);

 void uiDrawTransform(uiDrawContext *c, uiDrawMatrix *m);

// TODO add a uiDrawPathStrokeToFill() or something like that
 void uiDrawClip(uiDrawContext *c, uiDrawPath *path);

 void uiDrawSave(uiDrawContext *c);
 void uiDrawRestore(uiDrawContext *c);

// TODO manage the use of Text, Font, and TextFont, and of the uiDrawText prefix in general

///// TODO reconsider this
typedef struct uiDrawFontFamilies uiDrawFontFamilies;

 uiDrawFontFamilies *uiDrawListFontFamilies(void);
 int uiDrawFontFamiliesNumFamilies(uiDrawFontFamilies *ff);
 char *uiDrawFontFamiliesFamily(uiDrawFontFamilies *ff, int n);
 void uiDrawFreeFontFamilies(uiDrawFontFamilies *ff);
///// END TODO

typedef struct uiDrawTextLayout uiDrawTextLayout;
typedef struct uiDrawTextFont uiDrawTextFont;
typedef struct uiDrawTextFontDescriptor uiDrawTextFontDescriptor;
typedef struct uiDrawTextFontMetrics uiDrawTextFontMetrics;





typedef unsigned int uiDrawTextWeight; enum {
	uiDrawTextWeightThin,
	uiDrawTextWeightUltraLight,
	uiDrawTextWeightLight,
	uiDrawTextWeightBook,
	uiDrawTextWeightNormal,
	uiDrawTextWeightMedium,
	uiDrawTextWeightSemiBold,
	uiDrawTextWeightBold,
	uiDrawTextWeightUltraBold,
	uiDrawTextWeightHeavy,
	uiDrawTextWeightUltraHeavy,
};

typedef unsigned int uiDrawTextItalic; enum {
	uiDrawTextItalicNormal,
	uiDrawTextItalicOblique,
	uiDrawTextItalicItalic,
};


typedef unsigned int uiDrawTextStretch; enum {
	uiDrawTextStretchUltraCondensed,
	uiDrawTextStretchExtraCondensed,
	uiDrawTextStretchCondensed,
	uiDrawTextStretchSemiCondensed,
	uiDrawTextStretchNormal,
	uiDrawTextStretchSemiExpanded,
	uiDrawTextStretchExpanded,
	uiDrawTextStretchExtraExpanded,
	uiDrawTextStretchUltraExpanded,
};

struct uiDrawTextFontDescriptor {
	const char *Family;
	double Size;
	uiDrawTextWeight Weight;
	uiDrawTextItalic Italic;
	uiDrawTextStretch Stretch;
};

struct uiDrawTextFontMetrics {
	double Ascent;
	double Descent;
	double Leading;
	// TODO do these two mean the same across all platforms?
	double UnderlinePos;
	double UnderlineThickness;
};

 uiDrawTextFont *uiDrawLoadClosestFont(const uiDrawTextFontDescriptor *desc);
 void uiDrawFreeTextFont(uiDrawTextFont *font);
 uintptr_t uiDrawTextFontHandle(uiDrawTextFont *font);
 void uiDrawTextFontDescribe(uiDrawTextFont *font, uiDrawTextFontDescriptor *desc);
// TODO make copy with given attributes methods?
// TODO yuck this name
 void uiDrawTextFontGetMetrics(uiDrawTextFont *font, uiDrawTextFontMetrics *metrics);

// TODO initial line spacing? and what about leading?
 uiDrawTextLayout *uiDrawNewTextLayout(const char *text, uiDrawTextFont *defaultFont, double width);
 void uiDrawFreeTextLayout(uiDrawTextLayout *layout);
// TODO get width
 void uiDrawTextLayoutSetWidth(uiDrawTextLayout *layout, double width);
 void uiDrawTextLayoutExtents(uiDrawTextLayout *layout, double *width, double *height);

// and the attributes that you can set on a text layout
 void uiDrawTextLayoutSetColor(uiDrawTextLayout *layout, int startChar, int endChar, double r, double g, double b, double a);

 void uiDrawText(uiDrawContext *c, double x, double y, uiDrawTextLayout *layout);





 typedef unsigned int uiModifiers; enum {
	uiModifierCtrl = 1,
	uiModifierAlt = 2,
	uiModifierShift = 4,
	uiModifierSuper = 8,
};

// TODO document drag captures
struct uiAreaMouseEvent {
	// TODO document what these mean for scrolling areas
	double X;
	double Y;

	// TODO see draw above
	double AreaWidth;
	double AreaHeight;

	int Down;
	int Up;

	int Count;

	uiModifiers Modifiers;

	uint64_t Held1To64;
};

 typedef unsigned int uiExtKey; enum {
	uiExtKeyEscape = 1,
	uiExtKeyInsert,			// equivalent to "Help" on Apple keyboards
	uiExtKeyDelete,
	uiExtKeyHome,
	uiExtKeyEnd,
	uiExtKeyPageUp,
	uiExtKeyPageDown,
	uiExtKeyUp,
	uiExtKeyDown,
	uiExtKeyLeft,
	uiExtKeyRight,
	uiExtKeyF1,			// F1..F12 are guaranteed to be consecutive
	uiExtKeyF2,
	uiExtKeyF3,
	uiExtKeyF4,
	uiExtKeyF5,
	uiExtKeyF6,
	uiExtKeyF7,
	uiExtKeyF8,
	uiExtKeyF9,
	uiExtKeyF10,
	uiExtKeyF11,
	uiExtKeyF12,
	uiExtKeyN0,			// numpad keys; independent of Num Lock state
	uiExtKeyN1,			// N0..N9 are guaranteed to be consecutive
	uiExtKeyN2,
	uiExtKeyN3,
	uiExtKeyN4,
	uiExtKeyN5,
	uiExtKeyN6,
	uiExtKeyN7,
	uiExtKeyN8,
	uiExtKeyN9,
	uiExtKeyNDot,
	uiExtKeyNEnter,
	uiExtKeyNAdd,
	uiExtKeyNSubtract,
	uiExtKeyNMultiply,
	uiExtKeyNDivide,
};

struct uiAreaKeyEvent {
	char Key;
	uiExtKey ExtKey;
	uiModifiers Modifier;

	uiModifiers Modifiers;

	int Up;
};

typedef struct uiFontButton uiFontButton;
//TEST DOTDOTDOT
#define uiFontButton ...
// TODO document this returns a new font
 uiDrawTextFont *uiFontButtonFont(uiFontButton *b);
// TOOD SetFont, mechanics
 void uiFontButtonOnChanged(uiFontButton *b, void (*f)(uiFontButton *, void *), void *data);
 uiFontButton *uiNewFontButton(void);

typedef struct uiColorButton uiColorButton;
//TEST DOTDOTDOT
#define uiColorButton ...
 void uiColorButtonColor(uiColorButton *b, double *r, double *g, double *bl, double *a);
 void uiColorButtonSetColor(uiColorButton *b, double r, double g, double bl, double a);
 void uiColorButtonOnChanged(uiColorButton *b, void (*f)(uiColorButton *, void *), void *data);
 uiColorButton *uiNewColorButton(void);

typedef struct uiForm uiForm;
//TEST DOTDOTDOT
#define uiForm ...
 void uiFormAppend(uiForm *f, const char *label, uiControl *c, int stretchy);
 void uiFormDelete(uiForm *f, int index);
 int uiFormPadded(uiForm *f);
 void uiFormSetPadded(uiForm *f, int padded);
 uiForm *uiNewForm(void);



 typedef unsigned int uiAlign; enum {
	uiAlignFill,
	uiAlignStart,
	uiAlignCenter,
	uiAlignEnd,
};

  typedef unsigned int uiAt; enum {
	uiAtLeading,
	uiAtTop,
	uiAtTrailing,
	uiAtBottom,
};

typedef struct uiGrid uiGrid;
//TEST DOTDOTDOT
#define uiGrid ...
 void uiGridAppend(uiGrid *g, uiControl *c, int left, int top, int xspan, int yspan, int hexpand, uiAlign halign, int vexpand, uiAlign valign);
 void uiGridInsertAt(uiGrid *g, uiControl *c, uiControl *existing, uiAt at, int xspan, int yspan, int hexpand, uiAlign halign, int vexpand, uiAlign valign);
 int uiGridPadded(uiGrid *g);
 void uiGridSetPadded(uiGrid *g, int padded);
 uiGrid *uiNewGrid(void);
